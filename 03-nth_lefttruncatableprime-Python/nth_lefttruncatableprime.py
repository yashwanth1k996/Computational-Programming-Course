# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

def isprime(n):
    for i in range(2, n//2 + 1):
        if(n%i == 0):
            return False
    return True

def lefttruncate(n):
    list1 = []
    while(n > 0):
        list1.append(str(n%10))
        n = n//10
    for i in range(len(list1)-1, -1, -1):
        check = "".join(list1[i::-1])
        if(not isprime(int(check))):
            return False
    return True


def fun_nth_lefttruncatableprime(n):
    count = -1
    val = 2
    while(count <n):
        if(isprime(val)):
            if(lefttruncate(val)):
                count += 1
                if(count == n):
                    return val
        val+=1


print(fun_nth_lefttruncatableprime(4))