import sys
size=int(input())
arr=input();
arr=list(map(int,arr.split(" ")))
count=0
while count<=size:
	temp=arr[0]
	arr.remove(temp)
	if temp not in arr:
		print(temp)
		sys.exit()
	count+=1
print("-1")	
