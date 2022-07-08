#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp

# #if using termux
# import subprocess
# import shlex
# #end if

def uni_cdf(x):
	if x < 0:
		return 0.0
	elif x > 1:
		return 1.0
	else:
		return x

def qfunc(x):
	return (0.5 - 0.5*mp.erf(x/np.sqrt(2)))

def gau_cdf(x):
	return (1.0-qfunc(x)) 

def other_cdf(x):
	if x > 0:
		return (1.0-np.exp(-x/2))
	else:
		return 0.0

def tri_cdf(x):
	if x < 0:
		return 0.0
	elif x > 2:
		return 1.0
	elif x >= 0 and x <=1: 
		return (x**2)/2.0
	else:
		return (-x**2/2 + 2*x -1.0)
	


vec_other_cdf = np.vectorize(other_cdf)
vec_gau_cdf = np.vectorize(gau_cdf)
vec_tri_cdf = np.vectorize(tri_cdf)

x = np.linspace(-4,4,30)#points on the x axis
x2 = np.linspace(-4,4,1000)#points on the x axis


simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
randvar = np.loadtxt('/home/nitya/repos/RandAssig/codes/tri.dat',dtype='double')
# randvar = np.loadtxt('other.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

plt.plot(x.T,err,'o')#plotting the CDF
plt.plot(x2,vec_tri_cdf(x2))
# plt.plot(x.T,err,'o',color='grey')#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Empirical","Theorectical"])
# #if using termux
plt.savefig('/home/nitya/repos/RandAssig/figs/tri_cdf.pdf')
plt.savefig('/home/nitya/repos/RandAssig/figs/tri_cdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
# #if using termux
# plt.savefig('../figs/gauss_cdf.pdf')
# plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window