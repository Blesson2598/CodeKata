r,c=input().split(" ")
r=int(r);c=int(c)
# r=int(size[0]);c=int(size[1])
mat=[]
for i in range(r):
	s=input().rstrip()
	arr=list(map(int,s.split(" ")))
	mat.append(arr)
fin=[]
if r==1:
	print(*mat[i],sep=" ")
	exit()
for i in range(0,1):
	for j in range(c):
		for k in range(1,r):
			f=0
			if mat[i][j] in mat[k]:
				continue
			else:
				f=1
				break
		if f==0:
			fin.append(mat[i][j])
fin.sort()
print(*fin,sep=" ")
