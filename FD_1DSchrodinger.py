import numpy as np 
from scipy.linalg import eigh 

#we set mu = hbar = 1

xmin = -10; xmax = 10; Nmesh = 2000
xmesh = np.linspace(xmin, xmax, Nmesh)
h = xmesh[1] - xmesh[0]

L = 1.0
V = 8.0 
def Vpot(x):
    if abs(x)< L/2.:
        return -V
    else:
        return 0.
    
def buildH():
    Vx = np.array([Vpot(x) for x in xmesh])
    H = np.diag(Vx) 

    for i in range(Nmesh):
        H[i, i] += 1./(h*h)

    for i in range(Nmesh-1):
        H[i, i+1] += -0.5/(h*h)
        H[i+1, i] += -0.5/(h*h)
    
    return H 

if __name__=='__main__':

    H = buildH()
    w, v = eigh(H)

    print w[0:3]

    import matplotlib.pyplot as plt
    #plt.plot(xmesh, [Vpot(x) for x in xmesh], 'k-', lw=2)

    for n in range(3):
        plt.plot(xmesh, v[:,n], label='n=%g'%(n))
    plt.xlabel('$x$')
    plt.ylabel('$\Psi_{n}(x)$')
    plt.legend()
    plt.show()