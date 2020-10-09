# def uniqueChars(s):
#     ans = -1
#     lenghtCurrentString = 0
#     start = 0
#     buck = [0]*30
#     charInit = ord("a") 
#     for ch in s:
#         letterValue = ord(ch)-charInit
#         lenghtCurrentString+=1
#         if  buck[letterValue] > 0:
#             while buck[letterValue] > 0:
#                 currentStartChar = ord(s[start])-charInit
#                 buck[currentStartChar]-=1
#                 start+=1
#                 lenghtCurrentString-=1
#         buck[aux]+=1
#         ans = max(ans,lenghtCurrentString)
# #     return ans       

def uniqueChars(s):
    ans = -1
    lenghtCurrentString = 0
    start = 0
    buck = [0]*30
    charInit = ord("a") 
    for i in range(len(s)):
        letterValue = ord(s[i])-charInit
        lenghtCurrentString+=1
        if buck[letterValue] > 0:
            lenghtCurrentString-= buck[letterValue]-start
            start = buck[letterValue]
        buck[letterValue]=i
        ans = max(ans,lenghtCurrentString)
    return ans       
"""       
## ABCDEA
START = 0
I = 5
"""