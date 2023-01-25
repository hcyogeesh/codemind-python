n=int(input())
a=list(map(int,input().split()))
for i in range(n):
    c=0
    m=min(a)
    f=0
    for i in range(len(a)):
        if a[i]-m>=0:
            c+=1
    for i in a:
        if i==m:
            f+=1
    for i in range(f):
        a.remove(m)
    print(c)