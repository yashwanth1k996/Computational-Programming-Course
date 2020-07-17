"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct valuements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(arr,value):
    
    # First and last index values
    first = 0
    last = len(arr) - 1
    # found = False
    while first <= last:
        mid = (first+last)//2
        if arr[mid] == value:
            return mid
        else:
            if value < arr[mid]:
                last = mid -1
            else:
                first = mid + 1
                
    return -1


print(binary_search([1,3,9,11,15,19,29], 15))

