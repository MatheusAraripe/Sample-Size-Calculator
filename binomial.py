import math as mt

from scipy.stats import norm


#get the value from a standard normal table using the area of alpha(the probability)
def standard_normal(prob):
    z = norm.ppf(prob,0,1)
    return z


def binomial_sample_size(alpha,power,e):
   
    p1 = 0.5
    p2 = p1+(e*p1/100)

    beta = 1-power
    alpha = alpha/2

    z2 = standard_normal(beta)
    z1 = standard_normal(alpha)*-1

    a1 = mt.sqrt(p2*(1-p2))
    b1 = mt.sqrt(p1*(1-p1))

    a =  z2*a1
    b =  z1*b1
    c = p1-p2

    t = a-b

    n = ((t)/c)**2

    #return z1,z2,t,n
    return round(n)