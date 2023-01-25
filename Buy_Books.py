n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
s1,s2 = 0,0
for i in a:
    s1+=i
for i in b:
    s2+=i
if s1>s2:
    print(0)
else:
    print(s2-s1)