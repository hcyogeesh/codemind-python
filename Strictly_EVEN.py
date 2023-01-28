n = int(input())
lst = list(map(int,input().split()))

flag=1

for i in range(n):
    if i%2==1 and lst[i]%2==0:
        flag=0
        break
if flag:
    print("True")
else:
    print("False")