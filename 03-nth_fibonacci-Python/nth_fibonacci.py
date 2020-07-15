# Background: The Fibonacci numbers are defined by F(n) = F(n-1) + F(n-2). 
# There are different conventions on whether 0 is a Fibonacci number, 
# and whether counting starts at n=0 or at n=1. Here, we will assume that 
# 0 is not a Fibonacci number, and that counting starts at n=0, 
# so F(0)=F(1)=1, and F(2)=2. With this in mind, write the function 
# nthfibonaccinumber(n) that takes a non-negative int n and returns the nth Fibonacci number.

def fib(pos, f1, f2):
	if(pos == 1):
			return f2
	else:
			return fib(pos-1, f2, f1+f2)

def fun_nthfibonaccinumber(n):
	# your code goes Here
	if(n == 0 or n == 1):
    		return 1
	val = fib(n, 0, 1)
	return val



print(fun_nthfibonaccinumber(6))