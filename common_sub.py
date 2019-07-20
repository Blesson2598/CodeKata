size=int(input())
strs=[];min_str="";l=1000000
for i in range(size):
	s=input()
	strs.append(s)
	if len(s)<l:
		l=len(s)
		min_str=s
dec=1		
v=len(min_str)
temp=min_str[:]
while len(min_str)>=0:
	val=0
	for i in range(size):
		c=strs[i].count(min_str)
		if c==1:
			val+=1
	if val==size:
		print(min_str)
		exit()
	else:
		min_str=temp[0:v-dec]
		dec+=1
