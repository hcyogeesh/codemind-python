n=int(input())
l=[int(i) for i in input().split()]
c=0
for i in l:
    if i!=0:
        print(i,end=" ")
    elif i==0:
        c+=1
for i in range(c):
    print(0,end=' ')