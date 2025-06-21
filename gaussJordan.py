import numpy as np

# Input number of equations
n = int(input("Enter the number of equations: "))

# Input augmented matrix
A = []
for i in range(n):
    row = list(map(float, input(f"Enter coefficients and constant term for equation {i+1}, separated by spaces: ").split()))
    if len(row) != n + 1:
        raise ValueError("Each row must have n coefficients and 1 constant term.")
    A.append(row)

A = np.matrix(A)
print("\nThe augmented matrix is:")
print(A)

# Gauss-Jordan Elimination
for i in range(n):
    # Partial pivoting
    max_row = i + np.argmax(np.abs(A[i:, i]))
    A[[i, max_row]] = A[[max_row, i]]

    # Make the pivot element 1
    pivot = A[i, i]
    if pivot == 0:
        raise ValueError("Mathematical Error: Division by zero.")
    A[i] = A[i] / pivot

    # Make other elements in column zero
    for j in range(n):
        if j != i:
            A[j] = A[j] - A[i] * A[j, i]
 
print("\nThe reduced row echelon form (RREF) is:")
print(A)

# Extract solutions
print("\nThe solution is:")
for i in range(n):
    print(f"x{i+1} = {A[i, -1]}")
