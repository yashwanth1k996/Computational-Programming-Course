# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.


def isautomorphic(val):
	auto = val**2
	while(val != 0):
		if(val%10 != auto%10):
			return False
		val = val//10
		auto = auto//10
	return True





def nthautomorphicnumbers(n):
	# Your code goes here
	val = 0
	count = 0
	while(count<n):
		if(isautomorphic(val)):
			count += 1
			if(count == n):
				return val
		val += 1




print(nthautomorphicnumbers(10))