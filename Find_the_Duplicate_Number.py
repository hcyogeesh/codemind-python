n =int(input())

l = [int(i) for i in input().split()]
s = set(l)

for i in s:
    c = l.count(i)
    if c>1:
        print(i)
        break
