n=int(input())
l=[int(i) for i in input().split()]
for i in range(n):
    if i<n-1:
        print(max(l[i+1:]),end=" ")
    else:
        print("-1")