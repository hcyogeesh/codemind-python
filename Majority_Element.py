n=int(input())
l=[int(i) for i in input().split()]
x=[]
for i in l:
    if l.count(i)>n//2 and i not in x:
        print(i,end=' ')
        x.append(i)