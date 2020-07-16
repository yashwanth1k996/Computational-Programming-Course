# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

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

# def fun_nth_happy_number(n):
#     if(n == 0):
#         return 1
#     count = 0
#     val = 2
#     while(count != n):
#         if(happuNumber(val)):
#             count += 1
#             # print(val)
#             if(count == n):
#                 break
#         val += 1
#     return val

def isprime(val):
	count = 0
	for i in range(1,(val//2)+1):
		if(val % i == 0):
			count += 1
	if(count >1):
		return False
	else:
		return True


def fun_nth_happy_prime(n):
	if(n == 0):
			return 7
	count = 0
	val = 8
	while(count != n):
			if(isprime(val) and happuNumber(val)):
					count += 1
					if(count == n):
							break
			val += 1
	return val
	