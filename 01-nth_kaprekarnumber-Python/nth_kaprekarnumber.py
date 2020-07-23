# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math 

def isequal(val, n):
    for i in range(1, len(val)):
        if((int(val[:i]) + int(val[i:])) == n):
            return True
    return False


def iskaprekar(n):
    val = n**2
    vallen = len(str(val))
    mid = vallen//2
    strval = str(val)
    if(vallen == 1):
        if(val == n):
            return True
        else:
            return False
    if(isequal(strval, n)):
        return True
    else:
        return  False



def fun_nth_kaprekarnumber(n):
    count = -1
    val = 1
    while(True):
        if(iskaprekar(val)):
            count+=1
            if(count == n):
                return val
        val += 1


print(fun_nth_kaprekarnumber(2))