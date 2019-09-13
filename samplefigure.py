import matplotlib.pyplot as plt
import numpy

# For more detail about usin LaTeX in matplotlib see
# https://matplotlib.org/users/usetex.html
from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif', size=12)


def plotmodel(noise_factor, plot_type, filename, label_size, *args, **kwargs):
    """plots the function argument Y against the x linspace on the figure axis
    specified

    Arguments:
        noise_factor: the factor of noise applied to the model to generate the
        data

        plot_type:
            "height" sets the graph with labels for Height vs time
            "velocity" sets the graph with labels for Velocity vs time
        filename: must contain the filename, a set of empty braces for noise
        factor encoding, and the file type extension in a string,
        "examplename{}.pdf")
        label_size: the font size of the X and Y axis, used for scaling fonts
        up when using subfigures
    """
    fig, ax = plt.subplots(1, 1, figsize=(5, 4))

    if plot_type == "height":
        ax.plot(x, modelA, 'k-', label='Model A')
        ax.plot(x, modelB, 'k--', label='Model B')
        ax.plot(x, ydata, 'b.', label='Experimental')
    elif plot_type == "velocity":
        ax.plot(x[:-1], diffA/dx, 'k-', label='Model A')
        ax.plot(x[:-1], diffB/dx, 'k--', label='Model B')
        ax.plot(x[:-1], ydiff/dx, 'b.', label='Experimental')
    else:
        raise ValueError("Please enter a valid plot type")

    set_axis_style(ax, plot_type, label_size)
    plt.savefig((filename).format(str(noise_factor).replace('.', 'p')))


def set_axis_style(ax, plot_type, label_size, *args, **kwargs):
    """Sets the decoration for all the figures in this file.

    Arguments:

        ax: figure axis to apply changes to
        plot_type:
        "height" sets the graph with labels corresponding to Height vs time
        "velocity" sets the graph with labels corresponding to Velocity vs time
    """
    if plot_type == "height":
        ax.set_xlabel('Time / s', fontsize=label_size)
        ax.set_ylabel('Height / m', fontsize=label_size)
    elif plot_type == "velocity":
        ax.set_xlabel('Time / s', fontsize=label_size)
        ax.set_ylabel(r'Velocity /$m\cdot s^{_1}$', fontsize=label_size)
    else:
        raise ValueError("Please enter a valid plot type")

    # the legend starts to take over the graph when subfigures are used
    ax.legend(fontsize=label_size-2)
    plt.tight_layout()


x = numpy.linspace(0, 10)
modelA = 100 - x**2
modelB = 110 - 10*x
ydata = modelA + numpy.random.randn(len(x))*10

plt.figure(figsize=(5, 4))  # note figure size in inches
plt.plot(x, modelA, 'k-', label='Model A')
plt.plot(x, modelB, 'k--', label='Model B')
plt.plot(x, ydata, 'b.', label='Experimental')
plt.xlabel('Time / s')
plt.ylabel('Height / m')
plt.legend(fontsize=12)
# This ensures the bounding box is correct. If we don't call tight_layout
# sometimes elements get cut off on the edges.
plt.tight_layout()
plt.savefig('samplefigure.pdf')

# Lets investigate the effect of noise on our Model "A" and it's derivative
# For-loop structures are very useful for this type of sensitivty analysis
# However, we can create a function to do most of this for us with ease
# The functions are plotmodel() and set_axis_style() as above

diffA = numpy.diff(modelA)
diffB = numpy.diff(modelB)
dx = x[1]-x[0]

for index, value in enumerate([1.0, 10, 100]):
    ydata = modelA + numpy.random.randn(len(x))*value
    ydiff = numpy.diff(ydata)
    plotmodel(value, "height", "modelfigure_{}.pdf", 14)
    plotmodel(value, "velocity", "differentialfigure_{}.pdf", 14)
