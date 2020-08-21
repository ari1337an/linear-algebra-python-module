# Import Numpy
import numpy as np
import sympy as sm
from fractions import Fraction 
from decimal import Decimal

# Print Newline
def endl(cnt = 1):
    print('\n')
    pass

# Single Out Only Column
def get_column(arr, column):
    return arr[:,column-1].reshape(( arr.shape[0] ,1))

# Single Out Only Row
def get_row(arr, row):
    return arr[row-1,:].reshape(( 1 ,arr.shape[1]))

# Elemetary Row Operation
def ero(arr, type, arg1 = 0, arg2 = 0, arg3 = 0):
    if(type=='Exchange'):
        temp = np.array(arr[arg2-1])
        arr[arg2-1] = np.array(arr[arg1-1])
        arr[arg1-1] = np.array(temp)                                  # arg1 and arg2 exchange
    elif(type == 'Const'):
        arr[arg1-1] = Fraction(arg2).limit_denominator()*arr[arg1-1]  # Applying, const
    elif(type == 'ConstTime'):
        arr[arg1-1] = arr[arg1-1] + Fraction(arg3).limit_denominator()*arr[arg2-1]                  # Applying, Const of, Const
    pass

# Replace one column by (n x 1) matrix
def rep_col(arr1, arr2, arg1):
    A[:,arg1-1] =B[:,0]
    pass

# Determinant of A_n
def det_A_n(A,B,n):
    temp_A = np.array(A)
    temp_B = np.array(B)
    temp_A[:,n-1] = temp_B[:,0]
    return sm.Matrix(np.array(temp_A)).det()

# Determinant of A
def det_A(A):
    return sm.Matrix(np.array(A)).det()

# Print A Matrix
def debug(A):
    temp_A = sm.Matrix(np.array(A))
    return temp_A
