s=input()
e,o,c=[],[],0
for i in s:
    if i.isupper() or i.islower() or i.isdigit():
        if i.isdigit():
            a=int(i)
            if a%2==0:
                e.append(a)
            else:
                o.append(a)
    else:
        c+=1
a=len(e)
b=len(o)
x=min(a,b)
y=max(a,b)
if c%2!=0:
    for i in range(x):
        print(o[i],end='')
        print(e[i],end='')
    if len(e)>len(o):
        for i in range(x,y):
            print(e[i],end='')
    else:
        for i in range(x,y):
            print(o[i],end='')
else:
    for i in range(x):
        print(e[i],end='')
        print(o[i],end='')
    if len(e)>len(o):
        for i in range(x,y):
            print(e[i],end='')
    else:
        for i in range(x,y):
            print(o[i],end='')