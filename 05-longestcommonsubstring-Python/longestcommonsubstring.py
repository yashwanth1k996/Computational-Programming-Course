# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    # Yourcode goes here
    big = ""
    small = ""
    common = ""
    if(len(s1) < len(s2)):
        big = s2
        small = s1
    else:
        big = s1
        small = s2
    box = 1
    while(box < len(small)):
        for i in range(0, len(small) - box):
            if(small[i:i+box] in big):
                print(small[i:i+box])
                common = small[i:i+box]
        box += 1
    return common


print(longestcommonsubstring("abABC", "abcAB"))


