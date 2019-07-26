import math
def isprime(c):
	sq=int(math.sqrt(c))
	for i in range(2,sq+1):
		if c%i==0:
			return 0
	return 1		
		
	
	
start,end=list(map(int,input().split()));count=0
for i in range(start,end+1):
	temp=bin(i)
	temp=temp[2:]
	c=temp.count('1')
	f=isprime(c)
	if f==1 and c!=1:
		count+=1
print(count)		
		
