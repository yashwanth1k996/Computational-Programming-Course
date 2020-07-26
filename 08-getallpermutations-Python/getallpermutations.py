# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
from itertools import permutations


def permute(a, l, r, result):
	if(l == r):
		result.append(tuple(a))
	else:
		for i in range(l, r+1):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r, result)
			a[l], a[i] = a[i], a[l]
		result.sort()
		return result

def getallpermutations(x):
	# Your code goes here
	n = len(x)
	a = list(x)
	result = []
	return permute(a, 0, n-1, result)




print(getallpermutations("abc"))
print(list(permutations("abc")))