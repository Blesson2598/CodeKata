size,k=map(int,input().split())
arr=list(map(int,input().split()))
charged=int(input())
del arr[k]
act=sum(arr)//2
if act==charged:
	print("Bon Appetit")
else:
	print(abs(charged-act))
	
