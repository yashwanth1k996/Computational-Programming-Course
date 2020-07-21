# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the 
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers 
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem. 


def sol(n, list1, comp):
	if(comp > n):
		return list1
	else:
		if(comp**3 < n):
			list1.append(comp)
			return sol(n, list1, comp+1)
		else:
			return sol(n, list1, comp+1)


def recursion_powersof3ton(n):
	# Your code goes here
	if(abs(n) != n):
		return None
	else:
		list1 = []
		list1 = sol(n, list1, 1)
	if(list1 == []):
		return None
	return list1