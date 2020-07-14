# lineintersection(m1, b1, m2, b2)[5pts]
# Write the function lineintersection(m1, b1, m2, b2) that takes four int or float values representing the 2 lines:
#     y = m1*x + b1
#     y = m2*x + b2
# This function returns the x value of the point of intersection of the two lines. If the lines are parallel, or identical, the function should return None.

def lineintersection(m1, b1, m2, b2):
	# your code goes here
	a1 = m1
	b = -1
	c1 = b1
	a2 = m2
	c2 = b2

	den = a1*b - a2*b
	print(den)
	if(den == 0):
    		return None
	x = (c2*b - c1*b)/den
	return x
	y = (c1*a2 - c2*a1)/den


print(lineintersection(2, 13, 2, 14))

