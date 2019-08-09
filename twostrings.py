s=input();l=len(s);s=list(s);half=l//2
if l%2==0:
	first_half=s[0:half]
	second_half=s[half:]
	if first_half==second_half:
		print("YES")
	else:
		print("NO")
else:
	del s[half]
	half=len(s)//2
	first_half=s[0:half]
	second_half=s[half:]
	if first_half==second_half:
		print("YES")
	else:
		print("NO")
	
