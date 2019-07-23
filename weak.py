size=int(input());count=0
arr=input()
arr=list(map(int,arr.split(" ")))
for i in range(size):
	for j in range(i+1,size):
		for k in range(j+1,size):
			if arr[i]>arr[j]>arr[k]:
				count+=1
print(count)				
			
