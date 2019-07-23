size=int(input())
arr=input().rstrip()
arr=list(map(int,arr.split(" ")))
arr=arr[::-1]
print(*arr,sep="->")
