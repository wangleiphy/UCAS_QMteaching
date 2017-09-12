from scipy.optimize import bisect
from math import tan, sqrt, pi

r = 2.0 

def func(x, n):
    return x * tan(x - n*pi/2) - sqrt(r**2 - x**2)

for n in range(2):
    alpha = bisect(lambda x: func(x, n), n*pi/2, min((n+1)*pi/2, r))
    beta = sqrt(r**2 - alpha**2)

    energy = -2*beta**2
    print 'alpha, beta, energy: ', alpha, beta, energy
