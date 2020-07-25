# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def isprime(n):
	for i in range(2, n//2+1):
		if(n%i == 0):
			return False
	return True


def reverseset(x):
	x = str(x)
	if(x != '2'):
		for i in x:
			if(int(i)%2 == 0):
				return False
	for i in range(0, len(x)):
		if(not isprime(int(x[i:] + x[:i]))):
			return False
	return True



def nthcircularprime(n):
	# Your code goes here
	count = -1
	val = 1
	while(count < n):
		if(val == 11):
			val += 2
		if(isprime(val)):
			if(reverseset(val)):
				count += 1
				if(count == n):
					return val
		if(val > 2):
			val += 2
		else:
			val += 1
			
			

print(nthcircularprime(39))