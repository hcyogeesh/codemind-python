t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    c,f=1,0
    for i in s:
        if s.count(i)==1:
            res=i
            f=1
            break
    if f==1:
        print(res)
    else:
        print(-1)