#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

def qfunc(x):
	return (0.5 - 0.5*mp.erf(x/np.sqrt(2)))

def gau_cdf(x):
	return (1.0-qfunc(x)) 


vec_gau_cdf = np.vectorize(gau_cdf)


x2 = np.linspace(-4,4,1000)#points on the x axis
x = np.linspace(-4,4,30)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('gau.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x.T,err,'o')#plotting the CDF

plt.plot(x2,vec_gau_cdf(x2))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Empirical","Theory"])
plt.savefig('../figs/gau_cdf.pdf')
plt.savefig('../figs/gau_cdf.eps')

plt.show() #opening the plot window