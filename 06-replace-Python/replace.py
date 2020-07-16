# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	s = ""
	flag = False
	s2len = len(s2)
	s1len = len(s1)
	for i in range(0, s1len-s2len+1):
		if(s1[i:len(s2)+i] == s2):
			if(flag == True):
				s = s[:i]+s3+s1[(i+len(s2)) :]
				flag = True
			else:
				s = s1[:i]+s3+s1[(i+len(s2)) :]
				s1 = s
				flag = True
	if(flag == True):
		return s
	else:
		return s1

# print(fun_replace("hellrldowo23ufn348hf oincodnrld123", "rld", "     "))

"hell     owo23ufn348hf oincodn     123"
"hell     owo23ufn348hf oincodn     123"