size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
arr=arr[::-1]
print(*arr,sep="->")
