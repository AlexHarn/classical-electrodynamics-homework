import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams

rcParams['figure.figsize'] = 10, 5
rcParams['font.size'] = 15


def multi(r):
    return -1/(r**3)


def exact(r):
    return -2*(1/r - 1/np.sqrt(1 + r**2))


r = np.linspace(.1, 10, num=1000)
plt.plot(r, multi(r), label='Multipole Expansion')
plt.plot(r, exact(r), label='Exact Solution')
plt.ylim(-10, 1)
plt.xlim(0, 10)
plt.xlabel(r'$r/a$')
plt.ylabel(r'$4\pi \epsilon_0 a/q \cdot \phi$')
plt.legend()
# plt.show()
# exit()
plt.savefig('plot.png')
plt.clf()

r = np.linspace(.001, 10, num=1000)
plt.plot(r, multi(r)*r**3, label='Multipole Expansion')
plt.plot(r, exact(r)*r**3, label='Exact Solution')
# plt.ylim(-10, 1)
plt.xlim(0, 10)
plt.xlabel(r'$r/a$')
plt.ylabel(r'$4\pi \epsilon_0 a/q \cdot r^3 \cdot \phi$')
plt.legend()
# plt.show()
plt.savefig('asymptopic.png')
