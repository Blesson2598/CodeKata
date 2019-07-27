s=input();s=list(s);l=len(s)
temp=list(set(s))
final=[]
for i in range(l):
	if s[i] in temp:
		final.append(s[i])
		temp.remove(s[i])
print(*final,sep="")		
