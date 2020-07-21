# Write the function alternatingSum(L) that takes a possibly-empty list of numbers, 
# and returns the alternating sum of the list, where every other value is subtracted 
# rather than added. For example: alternatingSum([1,2,3,4,5]) returns 1-2+3-4+5 
# (that is, 3). If L is empty, return 0. You may not use loops/iteration in this problem.

def check_alternating(l , pos, sum1):
	if(pos == len(l)):
		return sum1
	if(pos%2 == 0):
		sum1 += l[pos]
		return check_alternating(l, pos+1, sum1)
	else:
		sum1 -= l[pos]
		return check_alternating(l, pos+1, sum1)


def fun_recursions_alternatingsum(l): 
	sum = check_alternating(l, 0, 0)
	return sum