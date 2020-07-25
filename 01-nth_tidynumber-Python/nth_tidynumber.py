# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def istidynumber(val):
    val = str(val)
    if(len(val) == 1):
        return True
    for i in range(0, len(val)-1):
        if(not (val[i] <= val[i+1])):
            return False
    return True




def fun_nth_tidynumber(n):
    val = 1
    count = -1
    while(count < n):
        if(istidynumber(val)):
            count += 1
            # print(val)
            if(count == n):
                return val
        val += 1


# print(fun_nth_tidynumber(15))