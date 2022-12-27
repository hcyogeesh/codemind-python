x = int(input())
l = list(map(int,input().split()))
n=int(input())
c=0
k=[]
for i in list(set(l)):
    for j in l:
        if i==j:
            c+=1
    if n==c:
        print(i,end=' ')
        k.append(i)
    c=0
if k==[]:
    print('-1')