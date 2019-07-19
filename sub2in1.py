s1,s2=input().split()
l1=len(s1)
l2=len(s2)
subs=[]
c=0
while c<l2:
	for i in range(1,l2+1):
		string=s2[c:c+i]
		if string not in subs and len(string)>=2:
			subs.append(string)
	c+=1	
l=len(subs)
f=0
for i in range(l):
	if subs[i] in s1:
		f=1
		print("yes")
		exit()
print("no")		
