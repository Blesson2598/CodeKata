s=input();
l=len(s)
c=0
subs=[]
while c<l:
	for i in range(1,l):
		v=s[c:c+i]
		if v not in subs:
			subs.append(v)
	c+=1		
l=len(subs);final=[];m=0
for i in range(l):
	v=subs[i][:]
	if v[0]>s[0] and len(v)>m:
		final.append(v)
		m=len(v)
print(final[len(final)-1])
