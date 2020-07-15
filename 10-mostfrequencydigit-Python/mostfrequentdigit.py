# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	# your code goes here
	m = str(abs(n))
	dictionary = {}
	for i in range(0, len(m)):
		if(m[i] in dictionary):
    			dictionary[m[i]] = dictionary[m[i]] + 1
		else:
    			dictionary[m[i]] = 1

	max = 1
	vals = []
	for j in dictionary.keys():
			if(dictionary[j] > max):
					max = dictionary[j]
					vals.clear()
					vals.append(int(j))
			if(dictionary[j] == max):
					vals.append(int(j))
	
	vals.sort()
	return vals[0]

