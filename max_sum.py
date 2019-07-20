size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
sum1=0;c=2;all_sum=[]
j=0
while j<size:
	sum1=0
	for i in range(0,size,c):
		sum1+=arr[i]
	all_sum.append(sum1)
	c+=1
	j+=1
j=0
c=2
while j<size:
	sum1=0
	for i in range(1,size,c):
		sum1+=arr[i]
	all_sum.append(sum1)
	c+=1
	j+=1
print(max(all_sum))	
	
