size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
count=0;m=0
temp=arr[:]
temp.sort()
for i in range(size):
	if temp[i]!=arr[i]:
		count+=1
print(count)		
