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
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.legend()
# This ensures the bounding box is correct. If we don't call tight_layout
# sometimes elements get cut off on the edges.
plt.tight_layout()
plt.savefig('samplefigure.pdf')
