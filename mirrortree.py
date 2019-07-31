class Node:
	def __init__(self,data):
		self.val=data
		self.left=None
		self.right=None
def insert(root,parent,node):
    if root is not None:
        if root.val==parent:
            if root.left is None:
                root.left=node
            elif root.right is None:
                root.right=node
        else:
            insert(root.left,parent,node)
            insert(root.right,parent,node)
def printright(root):
    if root is None:
        return
    if root.right is not None:
        print(root.val,end=" ")
    if root.right is not None:
        print(root.right.val)
        printright(root.right)
    else:
        return
def printleft(root):
    if root is None:
        return
    if root.left is not None:
        print(root.val,end=" ")
    if root.left is not None:
        print(root.left.val)
        printleft(root.left)
        
size=int(input())
if size==1:
    print(1)
    exit()
root=Node(1)
for i in range(size-1):
	parent,child=map(int,input().split())
	insert(root,parent,Node(child))
printright(root)
printleft(root)
