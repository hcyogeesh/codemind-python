for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    mx = [0] * n
    mn = [0] * n
    mx[0] = a[0]
    mn[n-1] = a[n-1]
    for i in range(1, n):
        mx[i] = max(mx[i-1], a[i])
    for i in range(n-2, -1, -1):
        mn[i] = min(mn[i+1], a[i])
    res = 0
    maxi = 0
    mini = 10 ** 12
    for i in range(n-1):
        maxi = max(maxi, a[i])
        mini = min(mini, a[i])
        if mx[i] < mn[i+1]:
            res += (maxi - mini)
            maxi = 0
            mini = 10 ** 12
    maxi = max(maxi, a[n-1])
    mini = min(mini, a[n-1])
    res += (maxi - mini)
    print(res)