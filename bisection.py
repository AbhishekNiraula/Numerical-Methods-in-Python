import numpy as np
import pandas as pd

def f(x):
    return np.exp(x) - 4 * np.sin(x)

a = float(input("Enter float approximation: "))
b = float(input("Enter initial float approximation: "))

if f(a)*f(b) > 0:
    print(f"no root lies in the interval ({a}) and ({b})")
else:
    e = float(input("Enter the tolerable error: "))
    N = int(input("Enter the max no. of iterations: "))
    itr = 1
    list = []
    while itr <= N:
        c = (a + b)/2
        list.append([itr, a, b, c, f(c).round(4)])
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        err = abs(b-a)
        if err < e:
            list = pd.DataFrame(list, columns=['Iteration', 'a', 'b', 'c', 'f(c)'])
            for _, row in list.iterrows():
                print(' '.join(str(x) for x in row))
                print()
                print()
            print(f'Appropriate root is {(a + b)/2} in iteration {itr}')
            break
        itr += 1
        
    if ( itr > N ):
        print(f'Solution does not come in {N} iteration!')