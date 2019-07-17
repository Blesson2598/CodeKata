size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
diff=[]
l=len(arr)
for i in range(l):
	diff.append(abs(arr[i]-0))
val=[]	
for i in range(l):
	for j in range(i+1,l):
		if diff[i]-diff[j]==0:
			val.append(arr[i])
			val.append(arr[j])
			val.sort()
			val=val[::-1]
			print(*val,sep=" ")
			exit()
