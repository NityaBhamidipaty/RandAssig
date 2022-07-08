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



plt.plot(x2,vec_gau_cdf(x2))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')

plt.show() #opening the plot window