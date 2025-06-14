import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

eqn = input("Enter the equation in x using Python syntax: ")

def F(x, eqn):
    return eval(eqn)

def f(x):
    return F(x, eqn)

def g(f, x, h=1e-10):
    return (f(x+h) - f(x-h)) / (2*h)

a = float(input(f"Enter your initial approximation: "))

if g(f, a) == 0:
    print("The derivative is zero. Choose another approximation.")
else:
    e = float(input(f"Enter the tolerable error: "))
    N = int(input("Enter the max number of iterations: "))
    itr = 1
    list = []
    while itr <= N:   
        b = a - (f(a) / g(f, a))
        if (g(f, b) == 0):
            print("The slope tends to zero. Hence the function does not converge.")
            break
        error = abs((b - a) / b)
        list.append([itr, a, f(a), g(f, a), b])
        if error <= e:
            print(f"The root is {b} in iteration {itr} with error {error}")
            list = pd.DataFrame(list, columns=['Iterations', 'Xn', 'f(Xn)', "f'(Xn)", 'Xn+1'])
            for _, row in list.iterrows():
                print(' '.join(str(x) for x in row))
                print()
                print()
            break
        a = b
        itr += 1
    if (itr > N):
        print(f"Solution does not converge in {itr} iterations")
    x = np.linspace(-5, 5, 1000)
    plt.plot(x, [f(i) for i in x], color='blue', label='f(x)')
    plt.plot(x, [g(f, i) for i in x], color='red', label="f'(x)")
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.legend()
    plt.grid(True)
    plt.title('Newton-Raphson Method Visualization')
    plt.show()
