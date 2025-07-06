#Curve Fitting -To fit the second degree curve y=a+by+cx**2 to the given data using least square method
# x : 1 2 3 4 5
# y : 1090 1220 1390 1625 1915

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

n = int(input('Enter number of data points: '))
X = np.array(list(map(float, input("Enter all the X data's: ").split())))
Y = np.array(list(map(float, input("Enter all the Y data's: ").split())))

A = [[n, np.sum(X), np.sum(X**2)],
     [np.sum(X), np.sum(X**2), np.sum(X**3)],
     [np.sum(X**2), np.sum(X**3), np.sum(X**4)]]

B = [[np.sum(Y)],
     [np.sum(X*Y)],
     [np.sum(X**2*Y)]]

coeff = solve(A, B)
a, b, c = coeff.flatten()

print(f"\nThe coefficient matrix A:\n{np.matrix(A)}")
print(f"\nThe column matrix B:\n{np.matrix(B)}")
print(f"\nThe curve of best fit is:\n\t y = {a:.4f} + {b:.4f}x + {c:.4f}x²")

x_vals = np.linspace(min(X) - 1, max(X) + 1, 300)
y_vals = a + b * x_vals + c * x_vals**2

plt.figure(figsize=(10, 6))
plt.scatter(X, Y, color='darkorange', edgecolor='black', s=80, label='Data Points')
plt.plot(x_vals, y_vals, color='royalblue', linewidth=2.5, label='Best Fit Curve')

plt.title('Quadratic Curve Fitting using Least Squares', fontsize=14)
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.tight_layout()

plt.show()