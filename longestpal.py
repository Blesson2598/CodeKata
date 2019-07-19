s=input()
l=len(s)
pals=""
c=0
remove_i=0
remove_j=0
max_len=0
while c<l:
	for i in range(1,l+1):
		string=s[c:c+i]
		rev=string[::-1]
		pal_len=len(string)
		if rev==string and pal_len>1:
			if pal_len > max_len:
				pals=string
				max_len=pal_len
				remove_i=c
				remove_j=c+i
	c+=1		
s=list(s)	
s[remove_i:remove_j]=""
print(len(s))	
