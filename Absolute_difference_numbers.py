n,x=map(int, input().split())

first = int(str(n)[:x])
last =int(str(n)[-x:])

print(abs(first-last))
