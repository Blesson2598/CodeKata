s1="dhoni"
s2=input()
val=list(set(s1)-set(s2))
if len(val)==0:
	print("yes")
else:
	print("no")
