left,right=map(str,input().split("|"))
append=input()
if len(left)==len(right):
	print("Impossible")
if len(left)==0:
	if len(append)==len(right):
		print(append,'|',right,sep="")
	else:
		print("Impossible")
if len(right)==0:
	if len(append)==len(left):
		print(append,'|',right,sep="")
	else:
		print("Impossible")		
if abs(len(left)-len(right))==1:
	if len(left)>len(right):
		right+=append
	else:
		left+=append
	print(left,'|',right,sep="")
