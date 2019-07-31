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
def mirror(node):  
    if (node == None): 
        return
    else: 
        temp = node  
        mirror(node.left)  
        mirror(node.right)  
        temp = node.left  
        node.left = node.right  
        node.right = temp  
def inorder(node) : 
    if node is None:
        return
    if node.left is not None:
        print(node.val,node.left.val)
    if node.right is not None:
        print(node.val,node.right.val)
    inorder(node.right)  
    inorder(node.left)  
size=int(input())
if size==1:
    print(1)
    exit()
root=Node(1)
for i in range(size-1):
	parent,child=map(int,input().split())
	insert(root,parent,Node(child))
mirror(root)
inorder(root)
