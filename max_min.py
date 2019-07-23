size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
count=0;m=0
if size==1:
	print("1")
	exit() 
for i in range(0,size):
	
	if i-1>0 and arr[i]>arr[i-1]:
		count+=1
	if i+1<size and arr[i]>arr[i+1] :
		count+=1	
print(count)		
