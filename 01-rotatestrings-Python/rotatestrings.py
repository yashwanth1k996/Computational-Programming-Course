# Write the function rotatestring(s, k) that takes a string s and a possibly-negative integer k. 
# If k is non-negative, the function returns the string s rotated k places to the left. 
# If k is negative, the function returns the string s rotated |k| places to the right. So, for example:
# assert(rotateString('abcd',  1) == 'bcda')
# assert(rotateString('abcd', -1) == 'dabc')



def fun_rotatestrings(s, n):
	if(n > 0):
		sol = ""
		for i in range(n, len(s)):
			sol += s[i]
		sol += s[:n]
	elif(n == 0):
		return s
	else:
		sol = ""
		for i in range(len(s)-abs(n), len(s)):
			sol += s[i]
		sol += s[:len(s)-abs(n)]
	return sol


