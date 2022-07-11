import matplotlib.pyplot as plt
import numpy as np

N=1000000
Y = np.loadtxt("/home/nitya/repos/RandAssig/codes/equiy.dat", dtype=float)

x = range(N)

plt.plot(x, Y, 'o')

plt.grid()

plt.xlabel('$n$')
plt.ylabel('$Y$')
plt.savefig('/home/nitya/repos/RandAssig/figs/scatter.pdf')
# plt.savefig('/home/nitya/repos/RandAssig/figs/scatter.png')

plt.show()