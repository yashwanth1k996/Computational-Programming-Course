# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.


def shortenlongruns(L, k):
	# Your code goes here
	list1 = []
	count = 0
	val = 0
	for i in range(0, len(L)):
		if(L[i] == 0):
			list1.append(L[i])
			val = L[i]
			count = 1
		else:
			if(L[i] == val):
				count += 1
				if(count < k):
					list1.append(L[i])
			else:
				val = L[i]
				list1.append(L[i])
				count = 1
	return list1
		
    			
print(shortenlongruns([2, 3, 5, 5, 5, 3], 3))
