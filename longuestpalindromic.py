"""
Find the longuest Palindromic substring 
>>> longestPalindrome("cbbd")
'bb'
"""
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    mem = []
    ans = 0
    ans_string = ""
    for x in range(len(s)):
        mem.append([])
        for y in range(len(s)):
            mem[x].append(0)
        mem[x][x] = 1
        ans = 1
        ans_string = s[x]
        
    for x in range(len(s)-1):
        if s[x] == s[x+1]:
            mem[x][x+1] = 1
            ans_string = s[x:x+2]
    for x in range(2,len(s)):
        for y in range(len(s)-x):
            if s[y] == s[y+x]:
                mem[y][y+x] = mem[y+1][x+y-1]
            if mem[y][y+x] == 1:
                ans = max(ans,x+1)
                ans_string = s[y:y+x+1]
    return ans_string