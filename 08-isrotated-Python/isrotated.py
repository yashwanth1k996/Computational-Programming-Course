# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g. 
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is 
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
	#Your code goes here
	if(len(str1) != len(str2)):
		return False
	j = 0
	for i in range(0, len(str1)):
		if(str1[i] == str2[j]):
			j += 1
		else:
			if(j!=0):
				j = 0
	if(str1 == str2):
		return True
	print(str2[j : ])
	print(str1[:len(str1)-j])
	if(str2[j : ] == str1[:j+1]):
		return True
	else:
		return False

print(isrotated("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "BCDEFGHIJKLMNOPQRSTUVWXYZA"))