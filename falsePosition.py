import numpy as np
import pandas as pd

def f(x):
    return x*np.exp(x) - np.sin(x)

x1 = float(input("Enter first approximation: "))
x2 = float(input("Enter second approximation: "))

if f(x1) * f(x2) >= 0:
    print(f"No root lies in the interval ({x1}) and ({x2})")
    
else:
    e = float(input("Enter the tolearable error: "))
    N = int(input("Enter the max no. of iterations: "))
    itr = 1
    rootpre  = x1
    list = []
    if f(x1) < 0:
        a = x1
        b = x2
    else:
        a = x2
        b = x1
    while itr <= N:    
        root = (a*f(b) - b*f(a)) / (f(b) - f(a))
        list.append([
            int(itr),
            a,
            b,
            f(a),
            f(b),
            root,
            f(root)
        ])
        
        if f(root) > 0:
            b = root
        else:
            a = root
        err = abs(root - rootpre)
        rootpre = root
        if err < e:
            print(f"Root is approximately {root} in iteration {itr}")
            list = pd.DataFrame(list, columns=['Iteration', 'a', 'b', 'f(a)', 'f(b)', 'root', 'f(root)'])
            for _, row in list.iterrows():
                print(' '.join(str(x) for x in row))
                print()
                print()
            break
        itr += 1
        
    if itr > N:
        print(f"Solution does not come in {N} iterations!")
