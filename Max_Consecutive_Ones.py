n=int(input())
l=[int(i) for i in input().split()]
x=[]
a=0
for i in l:
    if i==1:
        a=a+1
    else:
        x.append(a)
        a=0
    x.append(a)
#print(x)
print(max(x))