import numpy as np
import pandas as pd

def f(x):
    return x**3 + x**2 + x + 7

x1 = float(input("Enter the first initial guess (x1): "))
x2 = float(input("Enter the second initial guess (x2): "))

if f(x1) * f(x2) > 0:
    print(f"No root lies in the interval ({x1}) and ({x2})")
else:
    e = float(input("Enter the tolerable error: "))
    N = int(input("Enter the max number of iterations: "))
    itr = 1
    list = []
    while (itr <= N):
        x3 = (f(x2) * x1 - f(x1) * x2) / (f(x2) - f(x1))
        list.append([itr, x1, x2, f(x1), f(x2), x3])
        x1 = x2
        x2 = x3
        error = abs(x3 - x1)
        if error < e:
            list = pd.DataFrame(list, columns = ['Iteration', 'x1', 'x2', 'f(x1)', 'f(x2)', 'x3'])
            for _, row in list.iterrows():
                print(' '.join(str(x) for x in row))
                print()
                print()
            print(f"Root found: {x3} with error: {error}")
            break
        itr += 1
    
    if (itr > N):
        print(f"Solution does not converge in {N} iterations!")