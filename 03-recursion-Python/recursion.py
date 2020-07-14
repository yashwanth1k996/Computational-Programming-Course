"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def fib(position, f1, f2):
    if(position == 1):
        return f2
    
    val = fib(position-1, f2, f1+f2)
    return val



def get_fib(position):
    if(position == 0):
        return 0
    val = fib(position, 0, 1)
    return val


# print(get_fib(9))