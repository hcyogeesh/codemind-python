a=input()
b=list(a.split(","))
ans=""
r,r1=[],[]
for i in b:
    c=list(i.split(":"))
    x=c[0]
    y=c[1]
    l=len(x)
    for i in y:
        k=int(i)
        if k<=l:
            r.append(k)
    if len(r)!=0:
        m=max(r)
        ans+=x[m-1]
    else:
        ans+="X"
    for i in range(len(r)):
        r.pop()
print(ans)