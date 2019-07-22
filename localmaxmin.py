size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
count=0;m=0
temp=arr[:]
temp.sort()
if temp==arr:
	print(m)
	exit()
for i in range(1,size-1):
	count=0
	if arr[i]>arr[i-1]:
		count+=1
	if arr[i]<arr[i+1]:
		count+=1
	if count>m:
		m=count
print(m)		
		
