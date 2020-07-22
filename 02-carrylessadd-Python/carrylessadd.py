# carry less addition means a  normal addition with the carry from each column ignored. 
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add 
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function 
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their 
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
	x = str(x)
	y = str(y)
	lenx = len(str(x))
	leny = len(str(y))
	minlen = min(lenx, leny)
	res = ""
	for i in range(minlen-1, 0, -1):
		val = int(x[i]) + int(y[i])
		val = val%10
		res += str(val)
	if(lenx > leny):
		res = x[:minlen] + res[-1::-1]
	if(leny > lenx):
		res = y[:minlen] + res[-1::-1]
	if(lenx == leny):
		res = res[-1::-1]

	return int(res)
