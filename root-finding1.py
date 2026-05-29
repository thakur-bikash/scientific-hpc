import numpy as np 

def bisection1(f, a, b, N):
    for i in range(1, N):
        c = (a + b ) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return c

a = -1; b = 1;

def f(x):
    return x - np.cos(x)

for i in range(2, 100):
    root = bisection1(f, a, b, i)
    # print(f"The root of f(x) = x - cos(x) is {root} with {i} iterations.")
print("The root is ", root)
