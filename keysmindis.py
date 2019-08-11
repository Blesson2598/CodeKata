people,keys,destination=map(int,input().split())
people_list=list(map(int,input().split()))
keys_list=list(map(int,input().split()));flags=0;difference=list()
for i in people_list:
	if i < destination:
		for j in keys_list:
			if (j > i) and (j<destination):
				flags+=1
				keys_list.remove(j)
				break
	if i>destination:
		for j in keys_list:
			if (j < i) and (j>destination):
				flags+=1
				keys_list.remove(j)
				break
if flags==people:
	for i in people_list:
		difference.append(abs(i-destination))
	print(max(difference))
else:
	min_people=min(people_list)
	min_key=min(keys_list)
	distance=abs(min_people-min_key)
	distance+=abs(min_key-destination)
	print(distance)
