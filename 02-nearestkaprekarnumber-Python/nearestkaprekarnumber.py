# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.


def isequal(val, n):
    for i in range(1, len(val)):
        if((int(val[:i]) + int(val[i:])) == n and int(val[i:]) != 0):
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


def fun_nearestkaprekarnumber(n):
    vallow = 0
    valhigh = 0
    for i in range(n, 0, -1):
        if(iskaprekar(i)):
            vallow = i
            break
    j = n+1
    while(j > n):
        if(iskaprekar(j)):
            valhigh = j
            break
        j += 1
    if((n-vallow) > (valhigh-n)):
        return valhigh
    else:
        return vallow

print(fun_nearestkaprekarnumber(49))