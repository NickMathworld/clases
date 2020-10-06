class Tree:
    def __init__(self, num, left=None, right=None):
        self.num = num
        self.left  = left
        self.right = right
    def insert(self,num):
        next = Tree(0,None,None)
        if num < self.num:
            if self.left == None:
                self.left = Tree(num,None,None)
                return 0
            next = self.left
        else:
            if self.right == None:
                self.right = Tree(num,None,None)
                return 0
            next = self.right
        
        while next != None:
            if num < next.num:
                if next.left == None:
                    next.left = Tree(num,None,None)
                    next = next.left
                next = next.left
            elif num > next.num:
                if next.right == None:
                    next.right = Tree(num,None,None)
                    next = next.right
                next = next.right
        # if num < node.num:
        #     if node.left == None:   
        #         node.left = Tree(num,None,None)
        #         return 
        #     self.insert(num,node.left)
        # if num > node.num:
        #     if node.right == None:   
        #         node.right = Tree(num,None,None)
        #         return
        #     self.insert(num,node.right)
        return 0

def search(node,x):
    if node == None:
        return False
    if node.num == x:
        return True
    if node.num > x:
        return search(node.left,x)
    else:
        return search(node.right,x)

def in_order(node):
    if node == None:
        return
    in_order(node.left)
    print(node.num)
    in_order(node.right)

def longest_path(node:Tree)->int:
    if node == None:
        return 0
    maxLeft = 1
    maxRight = 1
    if node.left != None:
        maxLeft = 1+longest_path(node.left)
    if node.right != None:
        maxRight = 1+longest_path(node.right)
    return max(maxLeft,maxRight)


# root = Tree(2,None,None)
# # A->B->C->
# root.insert(1)
# root.insert(2)
# root.insert(3)
# root.insert(4)
# root.insert(5)
# root.insert(6)
# root.insert(7)
# root.insert(8)

# in_order(root)

# print(search(root,4))
# print( longest_path(root))



# 1 2 
## A ? B -> True:False
# A < B -> True:False

# 2 < 4+1+2+3 

def binary_search(arr:[],target:int)->int:
    n = len(arr)
    left = 0
    right = n-1
    #10
    #7 8 9 10
    #left = 1
    #right 10
    #(10+6)/2
    while(left<=right):
        middle = (left+right)//2
        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            left = middle+1
        if arr[middle] > target:
            right = middle-1
    return -1


##exponenciación binaria
##shortest common ancestor
input = [1,2,3,4,5,6,7,8,9,10,15,20,45,456,1000,1234]

print(binary_search(input,15444))