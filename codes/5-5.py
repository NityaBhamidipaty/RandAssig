import numpy as np

Y = np.loadtxt('/home/nitya/repos/RandAssig/codes/equiy.dat')

X = np.loadtxt('/home/nitya/repos/RandAssig/codes/equiy_ber.dat')

#generated y values for which X = 1
Y1 = Y[X == 1.0]
X1 = Y1[Y1<0] #predicted -1

print('P(X^ = -1 | X = 1) = ', np.size(X1)/np.size(Y1))

#generated y values for which X = -1
Y2 = Y[X == -1.0]
X2 = Y2[Y2>=0] #predicted 1

print('P(X^ = 1 | X = -1) = ', np.size(X2)/np.size(Y2))






