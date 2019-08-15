s1=list(input());l1=len(s1)
s2=list(input());l2=len(s2)
check=[];count=0
min_len=min(l1,l2);c=0
while len(check)<min_len:
	check.append(s1[c])
	diff1=l1//(c+1)
	diff2=l2//(c+1)
	temp="".join(map(str,check))
	str1=temp*diff1
	str2=temp*diff2
	if str1=="".join(map(str,s1)) and str2=="".join(map(str,s2)):
	   count+=1
	c+=1
print(count)	
	
	
