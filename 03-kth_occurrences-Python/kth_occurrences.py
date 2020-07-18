# Given a string str and an integer K, the task is to find the K-th most 
# frequent character in the string. If there are multiple characters that 
# can account as K-th the most frequent character then, print any one of them.


def fun_kth_occurrences(s, n):
	d = {}
	for i in s:
		if(i in d.keys()):
			d[i] += 1
		else:
			d[i] = 1
	val = list(d.values())
	val.sort(reverse=True)
	print(val)
	val = val[n]
	for j in d:
		if(d[j] == val):
			return j

print(fun_kth_occurrences("helllo woorld", 2))