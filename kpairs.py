size,val=input().split()
size=int(size);val=int(val)
arr=input().rstrip()
arr=list(map(int,arr.split(" ")))
li=[]
for i in range(size):
	if arr[i]<val:
		li.append(arr[i])
l=len(li);c=0
m=max(li)
while c<l-1:
	if (li[c]+m)==val:
		print("YES")
		exit()
	c+=1	
print("NO")		
