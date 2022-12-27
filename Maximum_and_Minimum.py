x = int(input())
l = list(map(int,input().split()))
c=0
n=1
k=[]
for i in l:
    for j in l:
        if i==j:
            c+=1
    if i==c:
        k.append(i)
    c=0
if k==[]:
    print('-1')
else:
    print(min(k),end=" ")
    print(max(k))