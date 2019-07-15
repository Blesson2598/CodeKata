s=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
l=len(arr)
for i in range(l):
	for j in range(i+1,l):
		for k in range(j+1,l):
			if arr[i]+arr[j]==arr[k]:
				print(arr[i],arr[j],arr[k])
