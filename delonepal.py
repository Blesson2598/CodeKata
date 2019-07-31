s=input();s=list(s)
l=len(s)
temp=s[::-1]
if temp==s:
    print("YES")
    exit()
j=l-1  
final=s[:]
for i in range(l-1):
    if s[i]!=s[j]:
        if s[i+1]==s[j]:
            del final[i]
            break
    j-=1    
temp=final[::-1]
if temp==final:
    print("YES")
else:
    print("NO")
