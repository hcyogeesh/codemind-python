n=int(input())
l=[int(i) for i in input().split()]
n1=int(input())
l1=[int(i) for i in input().split()]
a=int(input())
c=0
for i in range(n):
    if a>=l[i] and a<=l1[i]:
        c+=1
print(c)