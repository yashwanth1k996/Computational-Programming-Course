# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

def newNumber(n):
    sum = 0
    while n > 0:
        sum += (n%10)**2
        n = n//10
    return sum

def happuNumber(n):
    list1 = []
    while True:
        if(n == 1):
            return True
        if(n in list1):
            return False
        list1.append(n)
        n = newNumber(n)

def fun_nth_happy_number(n):
    if(n == 0):
        return 1
    count = 0
    val = 2
    while(count != n):
        if(happuNumber(val)):
            count += 1
            print(val)
            if(count == n):
                break
        val += 1
    return val

print(fun_nth_happy_number(3))	
