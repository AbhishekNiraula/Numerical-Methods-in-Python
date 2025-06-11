import numpy as np
import pandas as pd

def f(x):
    return np.arctan(x)

x0 = float(input("Enter the initial guess (x0): "))

e = float(input("Enter the tolerable error: "))
N = int(input("Enter the max number of iterations: "))
itr = 1
list = []

while (itr <= N):
    x1 = f(x0)
    list.append([itr, x0, x1])
    error = abs(x1 - x0)
    
    if error < e:
        list = pd.DataFrame(list, columns=['Iteration', 'x0', 'x1'])
        for _, row in list.iterrows():
            print(' '.join(str(x) for x in row))
            print()
        print(f"Root found: {x1} with error: {error}")
        break	
    itr += 1
    x0 = x1
    
if (itr > N):
    print(f"Solution does not converge in {N} iterations!")