# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.



def fun_interleave(s1,s2):
	s1len = len(s1)
	s2len = len(s2)
	minlen = min(s1len,s2len)
	s = ""
	i = 0
	while(i<minlen):
		s+=s1[i]
		s+=s2[i]
		i+=1
	if(s1len == minlen):
		s += s2[i:]
	else:
		s += s1[i:]

	return s
    		
# print(fun_interleave('a#', 'cD!f2'))