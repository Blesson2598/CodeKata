n=int(input())
val=3;c=0;prev=0;
for i in range(100):
	prev=val
	val+=2*c
	if n<=prev:
		diff=abs(n-prev)
		print(1+diff)
		exit()
	if c==0:
		c=3
	else:	
		c=c*2
	
