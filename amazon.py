size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
prod=1
for x in arr:
	prod*=arr[x]
for x in range(size):
	print(prod//arr[x],end=" ")
