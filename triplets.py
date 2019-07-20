size=int(input())
arr=input().rstrip()
arr=list(map(int,arr.split(" ")))
c=0
for i in range(size):
	for j in range(i+1,size):
		for k in range(j+1,size):
			if arr[i]<arr[j]<arr[k]:
				c+=1
print(c)				
