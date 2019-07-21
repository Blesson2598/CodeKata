row,col=input().split()
col=int(col)
values=input().rstrip()
values=list(map(int,values.split(" ")))
for i in range(col):
	nodes=input()
	nodes=list(map(int,nodes.split(" ")))
	temp=values[nodes[0]-1:nodes[1]]
	x=0
	l=len(temp)
	for j in range(l):
		x^=temp[j]
	print(x)
