import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input("Enter the equation in x using python numpy syntax: ")

def f(x):
    return eval(eqn) 

x1 = float(input("Enter the first initial guess (x1): "))
x2 = float(input("Enter the second initial guess (x2): "))

if f(x1) == f(x2):
    print(f"The value becomes infinite. Change initial values.")
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
        error = abs(f(x3))
        if error < e:
            list = pd.DataFrame(list, columns = ['Iteration', 'x1', 'x2', 'f(x1)', 'f(x2)', 'x3'])
            for _, row in list.iterrows():
                print(' '.join(str(x) for x in row))
                print()
                print()
            print(f"Root found: {x3} in iteration {itr} with error: {error}")
            break
        itr += 1
    
    if (itr > N):
        print(f"Solution does not converge in {N} iterations!")
        
    # x = np.linspace(-10, 10, 5000)
    # plt.plot(x, f(x), color='r', label=f'{f(x)}')
    # plt.axhline(0, 0, color='b')
    # plt.axvline(0, 0, color = 'b')
    # plt.title('Secant Method')
    # plt.legend()
    # plt.grid(True)
    # plt.show()