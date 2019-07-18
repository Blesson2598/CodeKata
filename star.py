n=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
star=[]
for i in range(n-1):
	temp=[]
	temp=arr[i+1:]
	m=max(temp)
	if arr[i]>m:
		star.append(arr[i])
star.append(arr[n-1])		
print(*star,sep=" ")		
print(max(arr))
