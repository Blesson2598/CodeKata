s1="dhoni"
s2=input()
val1=list(set(s1)-set(s2))
val2=list(set(s2)-set(s1))
val=len(val1)+len(val2)
if val==0:
	print("yes")
else:
	print("no")
