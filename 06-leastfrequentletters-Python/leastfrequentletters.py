# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def leastfrequentletters(s):
	# Your code goes here
	d = {}
	s = s.lower()
	for i in s:
		if(i in "abcdefghijklmnopqrstuvwxyz"):
			if(i in d.keys()):
				d[i] += 1
			else:
				d[i] = 1
	if(d == {}):
		return ""
	low = min(d.values())
	list1 = []
	for i in d.keys():
		if(d[i] == low):
			list1.append(i)
	# list1 = list1.sort()
	result = "".join(list1)
	return result


print(leastfrequentletters("aDq efQ? FB'daf!!!"))