# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.


def property(n):
	val = n**5
	val = str(val)
	for i in range(0,10):
		if(str(i) not in val):
			return False
	return True


def nthwithproperty309(n):
	# Your code goes here
	i = 0
	count = 0
	while(count <= n):
		i += 1
		if(property(i)):
			count += 1
		
	return i

print(nthwithproperty309(1))