# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

def ispalindrome(x):
	val = str(x)
	if(val[-1::-1] == str(x)):
		return True
	else:
		return False

def reverse(x):
	val = 0
	while(x > 0):
		val = (val*10) + (x%10)
		x = x//10
	return val

def islychrel(x):
	for i in range(0, 20):
		x = x + reverse(x)
		print(x)
		if(ispalindrome(x)):
			return False
	return True		
		

def nthlychrelnumbers(n):
	# your code goes here
	count = 0
	val = 190
	while(count < n):
		if(islychrel(val)):
			count += 1
			if(count == n):
				return val
		val += 1


print(islychrel(196))

