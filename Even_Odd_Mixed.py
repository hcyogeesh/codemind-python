n = int(input())
even=0
odd=0
mixed=0
while(n>0):
    d = n%10
    if d%2==0:
        even=1
    elif d%2==1:
        odd=1
    n= n//10

if even==1 and odd==0:
    print("Even")
elif odd==1 and even==0:
    print("Odd")
else:
    print("Mixed")
