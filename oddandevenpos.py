size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
for i in range(size):
	if i%2==0 and arr[i]&1:
		print(arr[i],end=" ")
	elif i&1 and arr[i]%2==0:
		print(arr[i],end=" ")
		
		
