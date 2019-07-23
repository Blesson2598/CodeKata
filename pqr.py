n,p,q,r=input().split()
n=int(n);p=int(p);q=int(q);r=int(r)
arr=input();values=[]
arr=list(map(int,arr.split(" ")))
for i in range(n):
	for j in range(i,n):
		for k in range(j,n):
			val=(p*arr[i])+(q*arr[j])+(r*arr[k])
			values.append(val)
print(max(values))			
			
