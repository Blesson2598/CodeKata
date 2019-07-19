points=[]
for i in range(4):
	v1,v2=input().split()
	points.append(int(v1))
	points.append(int(v2))
if len(set(points))>2:
	print("no")
else:
	print("yes")
