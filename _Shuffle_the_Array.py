n=int(input())
l=[int(i) for i in input().split()]
#a=int(input())
for i in range(n//2):
    print(l[i],l[n//2+i],end=" ")