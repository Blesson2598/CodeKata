size=int(input())
num=input();
num=list(map(str,num.split(" ")))
num.sort()
num=num[::-1]
num="".join(map(str,num))
num=int(num)
print(num)
