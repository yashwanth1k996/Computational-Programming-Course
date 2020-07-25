# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.
def primefactors(val):
    list1 = []
    while(val%2 == 0):
        list1.append(2)
        val = val//2
    for i in range(3, val//2+1):
        while(val%i == 0):
            list1.append(i)
            val = val//i
    if(val > 2):
        list1.append(val)
    return list1

def fun_nth_uglynumber(n):
    if(n == 0):
        return 1
    count = 0
    val = 2
    while(count < n):
        list2 = primefactors(val)
        flag = True
        for i in list2:
            if(i not in [2,3,5]):
                flag = False
        if(flag):
            count += 1
            if(count == n):
                return val

    
print(fun_nth_uglynumber(1))