size=int(input())
arr=input().rstrip()
arr=list(map(int,arr.split(" ")))
final=[1]*size
for i in range(1,size-1):
	if arr[i]>arr[i-1]:
		final[i]=final[i-1]+1
if arr[0]>arr[1]:
	final[0]=final[1]+1
if arr[size-1]>arr[size-2]:
	final[size-1]=final[size-2]+1
print(sum(final))	
