t=int(input())

while t:
    str=input()
    l=len(str)
    for i in range(0, l):
        s=str[i]
        if s.isdigit()==True:
            print("Yes")
            break
    else:
            print("No")
    t=t-1