# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then 
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

def permute(a, l, r, res):
	if(l == r):
		res.append(a)
		return res
	else:
		for i in range(0, r+1):
			a[l], a[i] = a[i], a[l]
			permute(a, l+1, r, res)
			a[l], a[i] = a[i], a[l]


def getallpermutations(x):
	# Your code goes here
	n = len(x)
	a = list(x)
	res = []
	return permute(a, 0, n-1, res)




permute(['a', 'b', 'c'], 0, 2, [])