n=int(input())
l=[int(i) for i in input().split()]
c=0
x=l.copy()
x.sort()
for i in range(n):
    if l[i]!=x[i]:
        c+=1
        inde=l.index(x[i])
        l[i],l[inde]=l[inde],l[i]
print(c)