import matplotlib.pyplot as plt
import numpy

# For more detail about using LaTeX in matplotlib see
# https://matplotlib.org/users/usetex.html
from matplotlib import rc

rc("text", usetex=True)
rc("font", family="serif")

# These figure sizes should correspond with the size in the LaTeX document.
# don't change the font size to compensate for scaling the figure down
aspect_ratio = 4 / 5
FULLSIZE = 5, 5 * aspect_ratio
HALFSIZE = 3, 3 * aspect_ratio

# Names and line types for the different plot series
YNAMES = "Model A", "Model B", "Experimental"
LINETYPES = "k-", "k--", "b."


def generate_data(noise_factor):
    """
    Generate some dummy data for the figure

    noise_factor: standard deviation of the noise
    """

    x = numpy.linspace(0, 10)
    modelA = 100 - x ** 2
    modelB = 110 - 10 * x
    ydata = modelA + numpy.random.randn(len(x)) * noise_factor

    return x, (modelA, modelB, ydata)


def samplefigure(x, ys, figsize, ylabel, legend=True):
    """
    Generate the sample figure

    x: x values for data
    ys: iterable of y values
    figsize: size of the figure in inches (width, height)
    ylabel: What the y label should be
    legend: Add a legend?
    """

    fig, ax = plt.subplots(1, 1, figsize=figsize)

    for y, linetype, label in zip(ys, LINETYPES, YNAMES):
        ax.plot(x, y, linetype, label=label)

    ax.set_xlabel("Time / s")
    ax.set_ylabel(ylabel)

    if legend:
        ax.legend()

    # This ensures the bounding box is correct. If we don't call tight_layout
    # sometimes elements get cut off on the edges.
    plt.tight_layout()


def plotfigure(noise_factor, figsize, filename, diff=False, legend=True):
    x, ys = generate_data(noise_factor)

    samplefigure(x, ys, figsize, "Height / m", legend)
    plt.savefig(filename.format(diff="model", noise_factor=noise_factor))

    if diff:
        diffys = [numpy.gradient(y, x) for y in ys]
        samplefigure(x, diffys, figsize, r"Velocity / m$\cdot$s$^{-1}$", legend)
        plt.savefig(filename.format(diff="derivative", noise_factor=noise_factor))


plotfigure(noise_factor=10, figsize=FULLSIZE, filename="graph/samplefigure.pdf")
plotfigure(noise_factor=10, figsize=HALFSIZE, filename="graph/samplefigure_halfsize.pdf")

# Lets investigate the effect of noise on our Model "A" and its derivative
# For-loop structures are very useful for this type of sensitivty analysis
# However, we can create a function to do most of this for us with ease

for noise_factor in [1, 10, 100]:
    plotfigure(
        noise_factor,
        figsize=HALFSIZE,
        filename="graph/noise_{noise_factor:03.0f}_{diff}.pdf",
        diff=True,
        legend=False,
    )
