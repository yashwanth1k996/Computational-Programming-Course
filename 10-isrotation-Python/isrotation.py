# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both 
# guaranteed to not contain any 0's, and 
# returns True if x is a rotation of the digits of y and False otherwise. For example, 
# 3412 is a rotation of 1234. Any number 
# is a rotation of itself.

def isrotation(x, y):
	# Your code goes here
	x = str(x)
	y = str(y)
	if(len(x) != len(y)):
		return False
	j = 0
	for i in range(0, len(x)):
		if(x[i] == y[j]):
			j += 1
		else:
			j = 0
	if(y[j:] == x[:len(x-j)]):
		return True
	else:
		return False