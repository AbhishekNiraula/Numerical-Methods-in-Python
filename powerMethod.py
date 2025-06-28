# Power Method to find the dominant eigenvalue and eigenvector
import numpy as np
import pandas as pd

# Input
n = int(input('Enter the order of matrix: '))
A = []

for i in range(n):
    A.append(list(map(float, input(f'Enter row {i+1}: ').split())))

A = np.array(A)
print('Matrix A:\n', A)

x = np.array(list(map(float, input('Enter initial guess vector: ').split())))
print('Initial vector:\n', x)

e = float(input('Enter tolerable error: '))
max_iter = int(input('Enter maximum number of iterations: '))

# Initialization
itr = 1
old_eigen = 0
table = []

while itr <= max_iter:
    y = np.dot(A, x)
    max_eigen = max(y, key=abs)
    x = y / max_eigen

    table.append([itr, max_eigen] + list(x))
    error = abs(max_eigen - old_eigen)

    if error < e:
        break

    old_eigen = max_eigen
    itr += 1

# Output
df = pd.DataFrame(table, columns=['Iteration', 'Eigen Value'] + [f'x{i+1}' for i in range(n)])
print("\nIteration Table:\n")
print(df.to_string(index=False))

if itr <= max_iter:
    print(f'\nConverged in {itr} iterations.')
    print(f'Dominant Eigenvalue: {max_eigen}')
    print('Corresponding Eigenvector:')
    print(x)
else:
    print('\nMethod did not converge within the given iterations.')
