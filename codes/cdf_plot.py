#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt

# #if using termux
# import subprocess
# import shlex
# #end if



x = np.linspace(-4,8,40)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('other.dat',dtype='double')
# randvar = np.loadtxt('other.dat',dtype='double')

for i in range(0,40):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x.T,err)#plotting the CDF
# plt.plot(x.T,err,'o',color='grey')#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

# #if using termux
plt.savefig('../figs/other_cdf.pdf')
plt.savefig('../figs/other_cdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
# #if using termux
# plt.savefig('../figs/gauss_cdf.pdf')
# plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window