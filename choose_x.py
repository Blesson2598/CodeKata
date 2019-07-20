n=int(input())
val=1
li=[]
for i in range(n-1,-1,-1):
	s=str(i)
	s=list(map(int,s))
	val=sum(s)
	if val+i==n:
		li.append(i)
		break
print(len(li))
print(*li,sep="\r")
