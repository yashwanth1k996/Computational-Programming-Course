# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

def digisum(n):
    dsum = 0
    while(n > 0):
        dsum += n%10
        n = n//10
    return dsum

def primefactors(n):
    list1 = []
    while(n%2 == 0):
        list1.append(2)
        n = n//2
    for i in range(3, n//2+1, 2):
        while(n%i == 0):
            list1.append(i)
            n = n//i

    if(n > 2):
        list1.append(n)
    print(list1)
    return list1

def issmith(n):
    nsum = digisum(n)
    pflist = primefactors(n)
    pfsum = 0
    for i in pflist:
        if(i > 9):
            pfsum += digisum(i)
        else:
            pfsum += i
    if(pfsum == nsum):
        return True
    else:
        return False
def fun_nth_smithnumber(n):
    count = -1
    val  = 4
    while(count != n):
        if(issmith(val)):
            count += 1
            if(count == n):
                return val

        val += 1

print(fun_nth_smithnumber(10))


# print(fun_nth_smithnumber(2))