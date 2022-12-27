x = int(input())
l = list(map(int,input().split()))
m=0
for i in sorted(set(l),key=l.index):
    if l.count(i)==i:
        print(i,end=" ")
        m=1
if m==0:
    print('-1')