"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    # Your code goes here
    min = 0
    max = len(input_array)-1
    mid = min+max // 2
    while(mid < len(input_array)):
        # print(input_array[mid])
        print(min, max)
        print(mid)
        if(value > input_array[mid]):
            min = mid
            mid = min+max // 2
            print(mid)
        elif(value < input_array[mid]):
            max = mid
            mid = max+min // 2
        else:
            return mid
    return -1


print(binary_search([1,3,9,11,15,19,29], 15))