marker_list=[0]*10000
size=int(input());Repeated_list=[]
arr=input();arr=list(map(int,arr.split(" ")))
print(arr)
arr.sort()
for i in range(size):
	marker_list[arr[i]]+=1
	if marker_list[arr[i]]>1 and arr[i] not in Repeated_list:
		Repeated_list.append(arr[i])
length=len(Repeated_list)
if length>0:
	print(*Repeated_list)
else:
	print("unique")
