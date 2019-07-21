size=int(input())
arr=input()
arr=list(map(int,arr.split(" ")))
bin_arr=[];max_one=0
for i in range(size):
	val=bin(arr[i])
	val=val[2:]
	bin_arr.append(val)
	if val.count('1')>max_one:
		max_one=val.count('1')
final=[];
while max_one>=0:
	temp=[]
	for i in range(size):
		if bin_arr[i].count('1')==max_one:
			temp.append(int(bin_arr[i],2))
	temp.sort()
	temp=temp[::-1]
	final.append(temp[:])
	max_one-=1
l=len(final)
for i in range(l):
	if len(final[i])>0:
		print(*final[i],sep="\r")
		
