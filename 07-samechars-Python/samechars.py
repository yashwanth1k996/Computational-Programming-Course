# sameChars(s1, s2) [20 pts]
# Write the function sameChars(s1, s2) that takes two strings and returns True if the two strings are composed of 
# the same characters (though perhaps in different numbers and in different orders) -- that is, if every character 
# that is in the first string, is in the second, and vice versa -- and False otherwise. This test is 
# case-sensitive, so "ABC" and "abc" do not contain the same characters. The function returns False if either 
# parameter is not a string, but returns True if both strings are empty (why?).

def samechars(s1, s2):
	# Your code goes here
	list1 = []
	list2 = []
	for i in s1:
		if(i not in list1):
			list1.append(i)
	for j in s2:
		if(j not in list2):
			list2.append(j)

	list1.sort()
	list2.sort()
	if(list1 == list2):
		return True
	else:
		return False



