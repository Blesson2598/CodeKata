s=input();lis1=[];l=len(s);f=0
for i in range(l):
	if s[i] not in lis1 and f==0:
		lis1.append(s[i])
	else:
		f=1;
print(len(lis1))		
