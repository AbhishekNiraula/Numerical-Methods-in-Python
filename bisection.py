import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - np.sin(x) - 9

a = float(input("Enter float approximation: "))
b = float(input("Enter initial float approximation: "))

if f(a)*f(b) > 0:
    print(f"no root lies in the interval ({a}) and ({b})")
else:
    e = float(input("Enter the tolerable error: "))
    N = int(input("Enter the max no. of iterations: "))
    itr = 1
    list = []
    list2 = []
    while itr <= N:
        c = (a + b)/2
        list.append([itr, a, b, c, f(c)])
        list2.append(c)
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        err = abs(b-a)
        if err < e:
            list = pd.DataFrame(list, columns=['Iteration', 'a', 'b', 'c', 'f(c)'])
            print(list.to_string(index = False))
            print(f'Appropriate root is {(a + b)/2} in iteration {itr}')
            break
        itr += 1
        
    if ( itr > N ):
        print(f'Solution does not come in {N} iteration!')
    x = np.linspace(-5 , 5, 1000)
    plt.plot(x, f(x), color='red', label='f(x)')
    plt.scatter(list2, f(list2), color = 'b')
    for i, val in enumerate(list2):
        plt.text(val, f(val), f'{i+1}')
    plt.axhline(0, 0, color='black')
    plt.axvline(0, 0, color='black')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Bisection Method')
    plt.legend()
    plt.show()