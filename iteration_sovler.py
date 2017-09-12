from numpy import tan , sqrt  

r = 2.0
def alpha2beta(alpha):
    return alpha* tan(alpha) 

def beta2alpha(beta):
    return sqrt(r*r - beta*beta)


if __name__=='__main__':

    alpha = 0.5
    for loop in range(10):
        beta = alpha2beta(alpha)
        print loop, alpha, beta 
        alpha = beta2alpha(beta)
        
