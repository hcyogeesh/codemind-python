n=int(input())
l=[int(i) for i in input().split()]
n1=int(input())
l1=[int(i) for i in input().split()]
x=[]
for i in range(n):
    a=l1[i]
    x.insert(a,l[i])
print(*x,sep=' ')