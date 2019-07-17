size=input()
arr1=input().rstrip()
arr2=input().rstrip()
arr1=list(map(int,arr1.split(" ")))
arr2=list(map(int,arr2.split(" ")))
diff=list(set(arr2)-set(arr1))
if len(diff)==0:
	print("YES")
else:
	print("NO")
