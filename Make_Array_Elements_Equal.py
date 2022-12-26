n=int(input())
a=list(map(int,input().split()));
if(len(set(a))==1):
    print(0)
else:
    c=0
    m=0
    for i in range(n):
        c=0
        for j in range(1,n):
            if a[i]==a[j]:
                c+=1
                if(m<c):
                    m=c
    print(m)