s=input()
l=len(s)
temp='ab'*l
subs=[];c=0
while c<l:
	for i in range(1,l):
		subs.append(s[c:c+i+1])
	c+=1
l=len(subs);m=0
for i in range(l):
	if subs[i] in temp:
		if len(subs[i])>m and subs[i][0]!='b' and len(subs[i])>1:
			m=len(subs[i])
print(m)			
		
