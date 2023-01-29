n, k, x, y = map(int, input().split())

mak=k*x
rem=abs(n-k)

if rem*x > rem*y:
    ab=rem*y
else:
    ab = rem*x

total=mak+ab

print(total)