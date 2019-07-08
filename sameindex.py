size=int(input())
arr=input();flag=0
arr=list(map(int,arr.split(" ")))
for i in range(size):
	if i==arr[i]:
		flag=1
		print(i,end=" ")
if flag==0:
	print("-1")
