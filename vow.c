s=input();
v="aeiouAEIOU";c="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ";
l=len(s)
for i in range(l):
	if s in v:
		print("Vowel");
	if s not in v and s in c:
		print("Consonant");
	if s not in v and c:
		print("invalid");
