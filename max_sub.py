size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
sub=[];max_len=0
for i in range(size):
	temp=[]
	temp.append(arr[i])
	m=max(temp)
	for j in range(i+1,size):
		if arr[j]>m:
			temp.append(arr[j])
			m=arr[j]
		else:
			break
	if len(temp)>max_len:
		max_len=len(temp)
print(max_len)		
	
	
