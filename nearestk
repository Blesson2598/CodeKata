def find_min(a,val):
	l=len(a)
	m=100000;ele=0
	for i in range(l):
		if abs(a[i]-val) < m and a[i]!=val:
			m=abs(a[i]-val)
			ele=a[i]
	a.remove(ele)
	return ele
	
size,k=input().split();size=int(size);k=int(k)
arr=input()
arr=list(map(int,arr.split(" ")))
f=find_min(arr,k)
print(f,end=" ")
f=find_min(arr,k)
print(f,end=" ")
f=find_min(arr,k)
print(f)
