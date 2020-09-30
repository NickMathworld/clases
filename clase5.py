# def lengtLastWord(s):
#     espacio = s.isspace()
#     if s == "":
#         return 0
#     if espacio == False:
#         res = s.split()
#         last = res[-1]
#         return len(last)
#     return 0


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        words = s.split(" ")
        print(words)
        length = len(words[-1])
        return length
s = Solution()

print(s.lengthOfLastWord(""))

arr1 = []
##arr1 -> ARREGLO, LISTA, PILA, COLA, DEQUEUE 
arr2 = [6,7,8,9,10]

arr1.append(0)
arr3 = arr1+arr2
arr3 = []

print(arr3)