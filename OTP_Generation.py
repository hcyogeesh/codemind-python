n=input()
i=0
a=len(n)
while n:
    a-=1
    if int(n[i])%2:
        print(int(n[i])**2,end='')
    i+=1