import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt

n = int(input("Enter the number of data points: "))
x = np.array(list(map(float, input("Enter all x's (space-separated): ").split())))
y = np.array(list(map(float, input("Enter all y's (space-separated): ").split())))

print("\nThe data points are:")
for i in range(n):
    print(f"({x[i]}, {y[i]})")

X = sp.symbols('x')    
xp = float(input("\nEnter the x value to interpolate: "))
s = 0

for i in range(n):
    lf = 1
    for j in range(n):
        if i != j:
            lf *= (X - x[j]) / (x[i] - x[j])
    s += y[i] * lf

poly = sp.simplify(s) 
print("\nLagrange Interpolation Polynomial:")
print(poly)

val = poly.subs(X, xp)
print(f"\nInterpolated value at x = {xp} is y = {val:.4f}")

x_plot = np.linspace(min(x), max(x), 300)
y_func = sp.lambdify(X, poly, modules='numpy')
y_plot = y_func(x_plot)

plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x_plot, y_plot, color='blue', label='Lagrange Curve') 
plt.scatter(xp, float(val), color='green', s=80, label=f'Interpolated Point ({xp:.4f}, {val:.4f})')

plt.title("Lagrange Interpolation")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
