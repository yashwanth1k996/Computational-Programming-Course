# triangleareabycoordinates(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function triangleareabycoordinates(x1, y1, x2, y2, x3, y3) that takes 6 int or float
# values that represent the three points (x1,y1), (x2,y2), and (x3,y3), and returns as a float the
# area of the triangle formed by those three points. Hint: you should make constructive use of
# the triangleArea function you just wrote above.

from math import sqrt

def distance(x1, y1, x2, y2):
	dist = sqrt((x1-x2)**2 + (y1-y2)**2)
	return dist

def triangleareabycoordinates(x1, y1, x2, y2, x3, y3):
	# your code goes here
	dist1 = distance(x1, y1, x2, y2)
	dist2 = distance(x2, y2, x3, y3)
	dist3 = distance(x3, y3, x1, y1)

	s = (dist1 + dist2 + dist3)/2

	return sqrt(s*(s-dist1)*(s-dist2)*(s-dist3))