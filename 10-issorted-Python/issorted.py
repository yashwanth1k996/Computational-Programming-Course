# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list 
# is sorted (either smallest-first or largest-first) and False otherwise. Your function 
# must only consider each value in the list once (so, in terms of big-oh, which we will 
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort 
# the list.

def issorted(a):
	# your code goes here
	if(len(a) == 1 or len(a) == 0):
		return True
	assendiing = False
	if(a[0] < a[1]):
		assendiing = True
	elif(a[0] == a[1]):
		if(a[1] < a[2] and len(a) >2):
			assendiing = True
	for i in range(0, len(a)-1):
		if(assendiing == True):
			if((a[i] < a[i+1]) == False):
				return False
		else:
			if((a[i] > a[i+1]) == False):
				return False
	return True

print(issorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))