size=input()
size=int(size)
arr=input()
arr=list(map(int,arr.split(" ")))
c=0
while c<size:
	half1=[]
	half2=[]
	if c+1<size:
		half1=arr[0:c+1]
	if c+1<size:
		half2=arr[c+1:]
	l1=len(half1)
	l2=len(half2)
	if l1>0 and l2>0:
		if((sum(half1)//l1)==(sum(half2)//l2)):
			print("yes")
			exit()
	c+=1	
print("no")		
