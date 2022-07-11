import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt

def qfunc(x):
	return (0.5 - 0.5*mp.erf(x/np.sqrt(2)))

def errorpr(a):
    bern = np.loadtxt('/home/nitya/repos/RandAssig/codes/equiy_ber.dat')
    gau = np.loadtxt('/home/nitya/repos/RandAssig/codes/gau.dat')

    Y = a*bern + gau

    #generated y values for which X = 1
    Y1 = Y[bern == 1.0]
    X1 = Y1[Y1<0] #predicted -1

    Pe0 = np.size(X1)/np.size(Y1)

    #generated y values for which X = -1
    Y2 = Y[bern == -1.0]
    X2 = Y2[Y2>=0] #predicted 1

    Pe1 = np.size(X2)/np.size(Y2)

    return (0.5*(Pe0+Pe1))

vec_errorpr = np.vectorize(errorpr)
vec_qfunc = np.vectorize(qfunc)

x = np.linspace(0,3,100)
x2 = np.linspace(0,3,10)
y = vec_qfunc(x)

plt.plot(x2, vec_errorpr(x2), 'o')
plt.plot(x,y)
plt.grid() #creating the grid
plt.xlabel('$A$')
plt.ylabel('$P_e(A)$')
plt.legend(["Numerical","Theoretical"])
plt.savefig('../figs/pevsa.pdf')
plt.show()



