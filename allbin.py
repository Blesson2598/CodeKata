n=int(input())
limit=pow(2,n)
final=[]
for i in range(limit):
	val=bin(i)
	val=val[2:]
	l=len(val)
	diff=n-l
	s='0'*diff
	li=[]
	li.append(s)
	li.append(val)
	final.append(s+val)
order=[]	
order.append(final[0])
c=1
while c<=n:
	for i in range(limit):
		if final[i].count('1')==c:
			order.append(final[i])
	c+=1		
print(*order,sep="\r")		
