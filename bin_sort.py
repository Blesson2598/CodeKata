size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
arr.sort()
arr=arr[::-1]
print(*arr,sep="\r")
