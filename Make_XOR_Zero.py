def xor(arr,data,add,n):
    r=0
    for i in arr:
        r^= ((i + data) & add)
    return r;
def solve(arr,n):
    add=1
    res=0
    maxim = max(arr)
    while add <= maxim:
        xr = xor(arr,res,add,n)
        if xr != 0:
            res += add
        add += 1
    xr = 0
    for i in arr:
        xr ^= (i + res)
    if xr == 0:
        return res
    return -1
n = int(input())
arr = list(map(int, input().split()))
print(solve(arr, n))