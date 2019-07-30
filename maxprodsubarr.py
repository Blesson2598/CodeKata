size=int(input())
arr=list(map(int,input().split()))
subs=[];c=0;m=0
while c<size:
	for i in range(1,size):
		temp=arr[c:i+c];
		p=1
		l=len(temp)
		for j in range(l):
			p*=temp[j]
		if p>m:
			m=p
	c+=1	
print(m)	
