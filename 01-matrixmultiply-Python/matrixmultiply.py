# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.

import numpy as np

def fun_matrixmultiply(m1, m2):
    rows1 = len(m1)
    rows2 = len(m2)
    col1 = len(m1[0])
    col2 = len(m2[0])
    if(col1 != rows2):
        return None
    mat = []
    for i in range(0, rows1):
        matin = []
        for j in range(0, col2):
            matin.append(0)
        mat.append(matin)
    for i in range(0, len(m1)):
        for j in range(0, len(m2[0])):
            for k in range(0, len(m2)):
                mat[i][j] += m1[i][k] * m2[k][j]
    return mat


print(fun_matrixmultiply([[1,3],[2,4],[2,5]], [[1,3,2,2], [2,4,5,1]]))
