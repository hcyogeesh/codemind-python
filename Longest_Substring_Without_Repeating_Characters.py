s=input()
x,y=[],[]
st=""
for i in s:
    if i.islower():
        a=i.upper()
    elif i.isupper():
        a=i.lower()
    if i not in st and a not in st:
        st+=i
    else:
        x.append(st)
        st=""
        st+=i
for i in x:
    y.append(len(i))
m=y[0]
r=0
for i in range(len(y)):
    if m < y[i]:
        m=y[i]
        r=i
if len(x[r])>2:
    print(x[r])
else:
    print(-1)