n=int(input())
l=[int(i) for i in input().split()]
t=int(input())
a=0
x=[]
for i in range(n):
    if t==l[i]:
        x.append(i)
        a+=1
        break
a=0
for i in range(n-1,-1,-1):
    if t==l[i]:
        x.append(i)
        a=a+1
        break
if a==0:
    print("-1 -1")
else:
    for i in x:
        print(i,end=" ")