class Tree:
    num = 0
    left = None
    right = None
    def __init__(self, num, left=None, right=None):
        self.num = num
        self.left  = left
        self.right = right

    
    def __str__(self):
        preOrder()
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
        return 0

def search(node,x):
    if node == None:
        return False
    print(node.num)
    if node.num == x:
        return True
    if node.num > x:
        return search(node.left,x)
    else:
        return search(node.right,x)

def inOrder(node):
    if node == None:
        return
    inOrder(node.left)
    print(node.num)
    inOrder(node.right)

root = Tree(2,None,None)
# A->B->C->
root.insert(1)
root.insert(4)
root.insert(2)
root.insert(3)
root.insert(5)
root.insert(8)
root.insert(15)
root.insert(-1)

#inOrder(root)

print(search(root,4))
