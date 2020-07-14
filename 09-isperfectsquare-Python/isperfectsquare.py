# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

def isperfectsquare(n):
	if(type(n) != int):
			return False
	for i in range(0, n//2):
		if(i**2 == n):
				return True
		else:
				return False



# print(isperfectsquare(6.25))