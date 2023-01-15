a,b,c=map(int, input().split())

for i in range(b,c+1):
    print("{} x {} = {}".format(a,i,a*i))