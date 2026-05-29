import numpy as np 

def f(x):
    return x - np.cos(x)

def bisection2(f, a, b, E_tol):
    E_max = (b - a) / 2 

    while E_max > E_tol:
        c = (a + b) / 2 
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c 

        E_max = (b - a) / 2 
    return c

a = -1; b = 1; E_tol = 10**(-16)
root = bisection2(f, a, b, E_tol)
print("The root is", root)
