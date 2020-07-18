# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2




def digsum(val):
	sum = 0
	while(val > 0):
		sum += val%10
		val = val // 10
	return sum

def isprime(val):
	count = 0
	for i in range(2, val//2+1):
		if(val % i == 0):
			count += 1
	if(count > 0):
		return False
	else:
		return True   		


def isadditiveprime(val):
	if(isprime(val)):
		sum = digsum(val)
		if(isprime(sum)):
			return True
		else:
			return False
	else:
		return False

def fun_nth_additive_prime(n):
	if(n == 0):
		return 2
	val = 2
	count = 0
	while(count < n):
		val += 1
		if(isadditiveprime(val)):
			count += 1
			
	return val