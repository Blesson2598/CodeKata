from itertools import permutations
s=input()
per=list(permutations(s))
for i in per:
	print(*i,sep="")
