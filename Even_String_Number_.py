s=input()
e,o,x,f=[],[],[],0
for i in s:
    if i.isdigit():
        a=int(i)
        if a not in e and a not in o:
            if a%2==0:
                e.append(a)
                f=1
            else:
                o.append(a)
e.sort(reverse=True)
for i in range(len(e)-1):
    x.append(e[i])
for i in o:
    x.append(i)
x.sort(reverse=True)
for i in range(len(e)):
    if i==(len(e)-1):
        x.append(e[i])
if f==1:
    for i in x:
        print(i,end="")
else:
    print(-1)