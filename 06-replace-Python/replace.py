# Without using the builtin method s.replace(), 
# write its equivalent. Specifically, write the function 
# replace(s1, s2, s3) that returns a string equal to 
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
	s = ""
	for i in range(0, len(s1)-len(s2)):
		if(s1[i:len(s2)+1] == s3):
			s = s+s1[:i+1]+s3+s1[(i+len(s2)+1) :]
			break
	return s

print(fun_replace("helloworld123", "hello", "345"))

