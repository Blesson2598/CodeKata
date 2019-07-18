size=int(input())
arr=[]
for i in range(size):
	s=input()
	s=list(map(int,s.split(" ")))
	l=len(s)
	for j in range(l):
		arr.append(s[j])
arr.sort()
print(*arr,sep=" ")		
