n,m = map(int,input().split())
b = []
for i in range(n):
    a = list(map(int,input().split()))
    b.append(a)
for i in range(m):
    s = 0
    for j in range(n):
        if s<b[j][i]:
            s=b[j][i]
    print(s)