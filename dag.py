final_sum=[]
class Node:
    def __init__(self,data):
        self.val=data
        self.child=[]
def insert(root,parent,node): 
    if root is None:
        root=node
    if root.val==parent:
        root.child.append(node)
    else:
        l=len(root.child)
        for i in range(l):
            if root.child:
                insert(root.child[i],parent,node)
            
            
def dfs(root,sum1):
    sum1+=root.val
    children=[]
    l=len(root.child)
    if not root.child:
        final_sum.append(sum1)
    for i in range(l):
        if root.child[i]:
            dfs(root.child[i],sum1)
    
nodes,edges=input().split()
nodes=int(nodes);edges=int(edges)
root=Node(1)
for i in range(edges):
    parent,child=input().split()
    parent=int(parent)
    child=int(child)
    insert(root,parent,Node(child))
sum1=0    
dfs(root,sum1)
print(max(final_sum))
