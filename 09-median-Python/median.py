# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	if(len(a) == 0):
		return None
	if(len(a) == 1):
		return a[0]
	if(len(a)%2 != 0):
		val = a[len(a)//2] + a[len(a)//2 + 1]
		val = val/2
	else:
		val = a[len(a)//2]
	return val

print(median([1, 2, 3, 4, 5]))