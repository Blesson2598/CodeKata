size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
sum1=0;c=size//2
while c>0:
	c-=1
	sum1+=max(arr)
	arr.remove(max(arr))
print(sum1)	
