left,right=map(str,input().split("|"))
append=input()
if len(left)==len(right):
	print("Impossible")
elif abs(len(left)-len(right))==1:
	if len(left)>len(right):
		right+=append
	else:
		left+=append
	print(left,'|',right,sep="")
else:
	print("Impossible")
