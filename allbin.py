n=int(input())
limit=pow(2,n)
for i in range(limit):
	val=bin(i)
	val=val[2:]
	l=len(val)
	diff=n-l
	s='0'*diff
	li=[]
	li.append(s)
	li.append(val)
	print(*li,sep="")
