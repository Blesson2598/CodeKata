size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
c=0;m=0;li=[]
while c<size:
	for i in range(1,size):
		val=arr[c:c+i]
		if val not in li:
			li.append(val)
	c+=1	
l=len(li)
for i in range(l):
	s=li[i][:]
	li[i].sort()
	if li[i]==s and m<len(li[i]):
		m=len(li[i])
print(m)		
		
