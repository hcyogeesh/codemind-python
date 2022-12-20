n = int(input())
flag=0
for i in range(n):
    if i*i==n:
        flag=1
        break;
if(flag):
    print("True")
else:
    print("False")
