s=input()
s=list(map(int,s.split(" ")))
arr=input()
arr=list(map(int,arr.split(" ")))
arr.sort()
arr=arr[::-1]
print(arr[s[1]-1])
