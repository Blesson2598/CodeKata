size=int(input())
arr=list(map(int,input().split()))
temp=arr[:];final=arr[:]
while len(arr)>1:
	for i in range(len(arr)):
		if i%2==0:
			temp.remove(arr[i])
	arr=temp[:]
print(final.index(arr[0]))	
