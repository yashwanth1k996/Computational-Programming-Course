# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of 
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say 
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
	# Your code goes here
	if(a == []):
		return []
	list1 = []
	val = 0
	count = 0
	for i in range(0, len(a)):
		if(val != a[i]):
			if(i != 0):
				list1.append((count, val))
			val = a[i]
			count = 1
		else:
			count += 1
	list1.append((count, val))
	return list1


print(lookandsay([1, 1, 1]))