# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

def reverseset(x):
	list1 = []
	x = str(x)
	for i in range(0, len(x)):
		list1.append(int(x[i:] + x[:i]))
	return list1


def isprime(n):
	for i in range(2, n//2+1):
		if(n%i == 0):
			return False
	return True
	



def nthcircularprime(n):
	# Your code goes here
	count = -1
	while(count < n):
		if(isprime(val)):
			list1 = reverseset(val)
			flag = True
			for i in list1:
				if(not isprime(i)):
					flag = False
					break
			if(flag):
				count += 1
				if(count == n):
					return val
			val += 1
