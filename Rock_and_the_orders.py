d,c=map(int, input().split())
a1, a2,a3=map(int, input().split())
b1,b2,b3 =map(int, input().split())

a = a1 + a2 + a3
b = b1 + b2 + b3

ca=cb=0
if a >= 150:
    ca = 1
if b >= 150:
    cb  =1
    
if ca and cb:
    cost_with_c = a+b+c
elif ca or cb:
    cost_with_c = a+b+c+d
elif ca==0 and cb==0:
    cost_with_c = a+b+d+d

cost_without_c = a+b+d+d

if cost_with_c < cost_without_c:
    print("YES")
else:
    print("NO")

