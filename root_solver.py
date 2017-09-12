from scipy.optimize import bisect
from math import tan , sqrt, pi

r = 2.0 

def func_even(x):
    return x * tan(x) - sqrt(r**2 - x**2)

def func_odd(x):
    return x / tan(x) + sqrt(r**2 - x**2)

for n in range(2):
    if (n%2==0):
        alpha = bisect(func_even, n*pi/2, min((n+1)*pi/2, r))
    else:
        alpha = bisect(func_odd, n*pi/2, min((n+1)*pi/2, r))

    beta = sqrt(r**2 - alpha**2)
    energy = -2*beta**2
    print n, alpha, beta, energy
