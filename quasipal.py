s=input()
rev=s[::-1]
if rev==s:
	print("yes")
	exit()
l=len(s);c=0;
for i in range(l-1,-1,-1):
	if s[i] =='0':
		c+=1
	else:
		break
zeros="0"*c
final=zeros+s
rev_final=final[::-1]
if rev_final==final:
	print("yes")
else:
	print("no")
