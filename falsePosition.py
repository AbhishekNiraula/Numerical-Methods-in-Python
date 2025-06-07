import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - np.sin(x) - 9

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
    list2 = []
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
        list2.append(root)
        
        if f(root) > 0:
            b = root
        else:
            a = root
        err = abs(root - rootpre)
        rootpre = root
        if err < e:
            print(f"Root is approximately {root} in iteration {itr}")
            list = pd.DataFrame(list, columns=['Iteration', 'a', 'b', 'f(a)', 'f(b)', 'root', 'f(root)'])
            print(list.to_string(index=False))
            break
        itr += 1
        
    if itr > N:
        print(f"Solution does not come in {N} iterations!")
    
    x = np.linspace(-5, 5, 1000)
    plt.plot(x, f(x), color='red', label='f(x)')
    plt.scatter(list2, f(np.array(list2)), color='b')
    for i, val in enumerate(list2):
        plt.text(val, f(val), f'{i+1}')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('False Position Method')
    plt.legend()
    plt.show()