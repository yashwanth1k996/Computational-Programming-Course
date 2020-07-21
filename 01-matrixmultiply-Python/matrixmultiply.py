# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    rows1 = len(m1)
    rows2 = len(m2)
    col1 = len(m1[0])
    col2 = len(m2[0])
    if(col1 != rows2):
        return None 




