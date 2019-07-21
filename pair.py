size,val=input().split()
size=int(size);val=int(val)
arr=input()
arr=list(map(int,arr.split(" ")))
for i in range(size):
	for j in range(i+1,size):
		if arr[i]+arr[j]==val:
			print("yes")
			exit()
print("no")			
