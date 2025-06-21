import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve
n = int(input("Enter the number of equations: "))

A = []
B = []
for i in range(n):
    row = list(map(float, input(f"Enter coefficients for equation {i+1}, separated by spaces: ").split()))
    if len(row) != n:
        raise ValueError("Each row must have n coefficients.")
    A.append(row)
    b = float(input(f"Enter the constant term for equation {i+1}: "))
    B.append(b)
    
A = np.matrix(A)
B = np.matrix(B)
print(f"\n The coefficient matrix A is: \n A = \n{A}")
print(f"\n The constant matrix B is: \n B = \n{B}")
P,L,U = lu(A)
lum = lu_factor(A)
print(f'The lower triangular matrix L is: \n{L}')
print(f'The upper triangular matrix U is: \n{U}')
print(f'The permutation matrix P is: \n{P}')
x = lu_solve(lum, B)
print(f'\nThe solution is: \n{np.round(x, 2)}')
