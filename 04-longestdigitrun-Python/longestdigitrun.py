# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns 
# the digit that has the longest consecutive 
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's), 
# as does longestDigitRun(-677886).
def longestdigitrun(n):
	# Your code goes here
	n = str(abs(n))
	count = 1
	maxcount = 0
	maxval = n[0]
	val = n[0]
	for i in range(1, len(n)):
		print(val)
		if(n[i] == val):
			count += 1
		else:
			if(count > maxcount):
				maxcount = count
				maxval = val
			if(count == maxcount):
				if(maxval > val):
					maxval = val
			val = n[i]
			count = 1
	return int(maxval)



print(longestdigitrun(44332211))