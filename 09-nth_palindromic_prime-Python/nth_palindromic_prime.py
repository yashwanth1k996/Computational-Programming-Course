# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def isprime(val):
	count = 0
	for i in range(2, val//2 + 1):
		if(val % i == 0):
			count += 1
	if(count > 0):
		return False
	else:
		return True

def ispalindrome(val):
	new = 0
	check = val
	while(check > 0):
		new = new * 10 + (check % 10)
		check = check // 10
	if(new == val):
		return True
	else:
		return False

def fun_nth_palindromic_prime(n):
	if(n == 0):
		return 2
	count = 0
	val = 2
	while(count < n):
		val += 1
		if(ispalindrome(val) and isprime(val)):
			count += 1
	return val
		