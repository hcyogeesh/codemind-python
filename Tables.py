n, x = input().split()
n=int(n)
x = int(x)

for i in range(1,x+1):
    if i % 2 == 0:
        continue
    else:
        print(str(n) + " x " + str(i) + " = " + str(n*i))