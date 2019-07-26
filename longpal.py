s=input();l=len(s)
subs=[];c=1
while c<l:
	for i in range(0,l):
		temp=s[i:i+c+1]
		subs.append(temp)
	c+=1
l=len(subs)
pal=['1']
for i in range(l):
	temp=subs[i][:]
	temp=temp[::-1]
	if subs[i]!=temp and len(temp)>len(pal[0]):
		pal.remove(pal[0])
		pal.append(subs[i])
print(*pal,sep="")	
