import matplotlib.pyplot as plt
import numpy

x = numpy.linspace(0, 10)
modelA = 100 - x**2
modelB = 110 - 10*x
ydata = modelA + numpy.random.randn(len(x))*10

plt.plot(x, modelA, 'k-', label='Model A')
plt.plot(x, modelB, 'k--', label='Model B')
plt.plot(x, ydata, 'b.', label='Experimental')
plt.xlabel('Time (s)')
plt.ylabel('Height (m)')
plt.legend()
plt.savefig('samplefigure.pdf')
