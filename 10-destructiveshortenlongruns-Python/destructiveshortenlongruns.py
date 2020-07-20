# Here we will rewrite the previous function to be destructive. This version must not just call the nondestructive 
# version from above and then clear and replace the values in the original list. Instead, you must traverse the list 
# once and make the changes to the list as you go. With that in mind, write the destructive function shortenLongRuns(
# L, k) that takes a list L and a positive integer k, and destructively modifies L by removing any values in L that 
# would otherwise produce a run of k consecutive equal values in L. 
# For example:
# L = [2, 3, 5, 5, 5, 3] 
# shortenLongRuns(L, 2)
# assert(L == [2, 3, 5, 3])
# And: 
# L = [2, 3, 5, 5, 5, 3]
# shortenLongRuns(L, 3)
# assert(L == [2, 3, 5, 5, 3])

def destructiveshortenlongruns(L, k):
	# Your code goes here
	val = 0
	count = 0
	x = L.copy()
	popped = 0
	for i in range(0, len(L)):
		if(i == 0):
			val = x[i]
			count += 1
		else:
			if(val == x[i]):
				count += 1
				if(count >= k):
					L.pop(i-popped)
					popped+=1
			else:
				val = x[i]
				count = 1
	return L


print(destructiveshortenlongruns([2, 3, 6, 6, 6, 3], 3))