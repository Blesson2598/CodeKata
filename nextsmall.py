from itertools import permutations
s=input();
temp=list(permutations(s))
s=int(s);final=[]
for x in temp:
	ss="".join(map(str,x))
	ss=int(ss)
	final.append(ss)
final.remove(s)
final.sort()
l=len(final)
for i in range(l):
	if final[i]>s:
		print(final[i])
		exit()
print("impossible")
