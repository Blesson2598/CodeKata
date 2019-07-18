size,val=input().split()
size=int(size);val=int(val)
arr=input();count=0
arr=list(map(int,arr.split(" ")))
arr.sort()
arr=arr[::-1]
l=len(arr)
for i in range(l):
	if val%arr[0]==0:
		count+=val//arr[0]
		val=0
	else:
		if arr[0]<=val:
			count+=val//arr[0]
			val=val%arr[0]
	arr.remove(arr[0])	
print(count)		
