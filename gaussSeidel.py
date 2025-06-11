import numpy as np
import pandas as pd

#Check if the matrix is diagonal dominant
def check_diaDom(A):
    r = len(A)
    # Always good idea to see if the code is working the way it should be
    # so, I have included print option to check throughout the process
    diagnl = 0
    non_diagnl = 0

    for i in range(r):
        for j in range(r):
            # print(f'Loop i = {i}, j = {j}\n')
            # print(A[i, j])
            if i ==j:
             diagnl+=abs(A[i] [j])
            elif i !=j: #here you can simply use else rather than else if
             non_diagnl+=abs(A[i] [j])
    
    # print('Sum of diagonal elements\n', diagnl)
    # print('Sum of non-diagonal elements\n', non_diagnl)

    if diagnl >=non_diagnl:
       verdict = True
       #print('Diagonal dominant Matrix')
    else:
       #print('Non-diagonal dominant Matrix')
       verdict = False
    return verdict

def GS_method(A, Y, X):
    n = len(A) # to find no of rows or col of sq matrix A
    for j in range(0, n):
        #old_val = X[i]
        summ_val = Y[j]
        for i in range(0, n):
            if (j!=i):
                summ_val-=A[j] [i] * X[i]
                #print(summ_val)
        X[j] = summ_val/A[j][j]
        #print(X[i]) 
    return X


A = [[10, -2, -1, -1],[-2, 10, -1, -1],[-1, -1, 10, -2], [-1, -1, -2, 10]] #coefficient of unknown variables
Y = [3, 15, 27, -9] #terms that appears after '=' sign in the equation
X = [0, 0, 0, 0] #initial guess for our method

if check_diaDom(A)==1:
 for i in range(1000):
    X = GS_method(A, Y, X)
    print(X)
else: 
   print('Non-Diagonal matrix')