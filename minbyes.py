n=int(input())
val=0;c=1;prev=0
while val<=n:
	val=pow(2,c)
	prev=pow(2,c-1)
	c+=1
print(abs(prev-n))
