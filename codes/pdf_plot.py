#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt

# #if using termux
# import subprocess
# import shlex
# #end if

def gauss_pdf(x):
	return 1/mp.sqrt(2*np.pi)*np.exp(-x**2/2.0)

def tri_pdf(x):
	if x < 0 or x > 2:
		return 0.0
	elif x>=0 and x <= 1.0:
		return x
	else :
		return 2.0 - x

def squgau(x):
	if x < 0.0:
		return 0.0
	else:
		return (0.5*np.exp(-0.5*x))

def sqrsqgau(x):
	if x < 0:
		return 0.0
	else:
		return x*np.exp(-x**2/2.0)

vec_tri_pdf = np.vectorize(tri_pdf)	
vec_gauss_pdf = scipy.vectorize(gauss_pdf)
vec_squgau_pdf = np.vectorize(squgau)
vec_sqrsqgau_pdf = np.vectorize(sqrsqgau)

maxrange=50
maxlim=4.0
x = np.linspace(-maxlim,maxlim,maxrange)#points on the x axis
x2 = np.linspace(-maxlim, maxlim, 10000)
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1)
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
randvar = np.loadtxt('/home/nitya/repos/RandAssig/codes/sqsqgau.dat',dtype='double')
# randvar = np.loadtxt('/home/nitya/repos/RandAssig/codes/tri.dat',dtype='double')
# randvar = np.loadtxt('/home/nitya/repos/RandAssig/codes/equi.dat',dtype='double')
# randvar = np.loadtxt('gau.dat',dtype='double')

for i in range(0,maxrange):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list
		

plt.plot(x[0:(maxrange-1)].T,pdf,'o')
plt.plot(x2,vec_sqrsqgau_pdf(x2))#plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$A$')
plt.ylabel('$f_A(a)$')
plt.legend(["Numerical","Theory"])

#if using termux
plt.savefig('/home/nitya/repos/RandAssig/figs/sqrsqugau_pdf.pdf')
plt.savefig('/home/nitya/repos/RandAssig/figs/sqrsqugau_pdf.pdf')

# plt.savefig('./../figs/squgau_pdf.pdf')
# plt.savefig('./../figs/squgau_pdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_pdf.pdf"))
#if using termux
# plt.savefig('/home/nitya/repos/RandAssig/figs/tri_pdf.pdf')
# plt.savefig('../figs/equi_pdf.eps')
# subprocess.run(shlex.split("termux-open ../figs/gauss_pdf.pdf"))
#else
plt.show() #opening the plot window
