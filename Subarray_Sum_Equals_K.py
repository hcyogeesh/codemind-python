n,t=map(int,input().split())
l=[int(i) for i in input().split()]
c=0
for i in range(n):
    s=0
    for j in range(i,n):
        s=s+l[j]
        if s==t:
            c+=1
        if s>t:
            break
print(c)