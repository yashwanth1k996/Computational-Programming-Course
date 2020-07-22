# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22



def digsum(n):
    sum = 0
    while(n > 0):
        sum += n%10
        n = n//10
    return sum


def isprime(n):
    for i in range(2, n//2 + 1):
        if(n%i == 0):
            return False
    return True


def issmith(n):
    list1 = []
    for i in range(2, n//2 + 1):
        if(n%i == 0 and isprime(i)):
            list1.append(i)
    nsum = digsum(n)
    listsum = 0
    for i in list1:
        listsum += digsum(i)
    if(listsum == nsum):
        return True
    else:
        return False



def fun_nth_smithnumber(n):
    if(n == 0):
        return 4
    val = 4
    count = 0
    while(count != n):
        val += 1
        if(issmith(val)):
            count += 1
    return val

print(issmith(27))

print(fun_nth_smithnumber(2))