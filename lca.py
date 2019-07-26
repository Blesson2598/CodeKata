size=int(input())
arr=list(map(int,input().split()))
val1,val2=map(int,input().split())
ind1=arr.index(val1)
ind2=arr.index(val2)
if abs(ind1-ind2)==1:
	print(min(val1,val2))
else:
	print(arr[0])
	
