def find(row,cos):
    que=[]
    for x in arr[row]:
        if x !=0:
            que.append(x)
    while 1:
        if len(que)==0:
            break
        else:
            index=arr[row].index(que[0])
            cos+=arr[row][index]
            del que[0]
            if index==n:
                cost.append(cos)
                return
            find(index,cos)        
        
n,m=map(int,input().split())
arr=[]
for i in range(n+1):
    temp=[0]*6
    arr.append(temp)
queue=[]    
for i in range(m):
    r,c,w=map(int,input().split())
    arr[r][c]=w
    if r==1:
        queue.append(w)
cost=[]     
while 1:
    cos=0
    if len(queue)==0:
        break
    else:
        index=arr[1].index(queue[0])
        cos+=arr[1][index]
        del queue[0]
        find(index,cos)
if len(cost)==0:
    print("-1")
    exit()
print(min(cost))        
        
        
