import matplotlib.pyplot as plt
import numpy

# For more detail about usin LaTeX in matplotlib see
# https://matplotlib.org/users/usetex.html
from matplotlib import rc
rc('text', usetex=True)
rc('font', family='serif')#, size=12)

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
plt.legend()
# This ensures the bounding box is correct. If we don't call tight_layout
# sometimes elements get cut off on the edges.
plt.tight_layout()
plt.savefig('samplefigure.pdf')

#Lets investigate the effect of noise on our Model "A" and it's derivative
for index, value  in enumerate([1.0, 10, 100]):
    ydata = modelA + numpy.random.randn(len(x))*value
    diffA = numpy.diff(modelA)
    ydiff = numpy.diff(ydata)
    dx = x[1]-x[0]
    
    plt.figure(figsize=(5, 4))  # note figure size in inches
    plt.plot(x, modelA, 'k-', label='Model A')
    plt.plot(x, modelB, 'k--', label='Model B')
    plt.plot(x, ydata, 'b.', label='Experimental')
    plt.xlabel('Time / s')
    plt.ylabel('Height / m')
    plt.legend()
    plt.tight_layout()
    plt.savefig(('modelfigure_{}.pdf').format(index))
    
    plt.figure(figsize=(5, 4))  # note figure size in inches
    plt.plot(x[:-1], diffA/dx, 'k-', label='Model A time differential ')
    plt.plot(x[:-1], ydiff/dx, 'b.', label='Experimental time differential ')
    plt.xlabel('Time / s')
    plt.ylabel(r'Velocity /$m\cdot s^{_1}$')
    plt.legend()
    # This ensures the bounding box is correct. If we don't call tight_layout
    # sometimes elements get cut off on the edges.
    plt.tight_layout()
    plt.savefig(('differentialfigure_{}.pdf').format(index))