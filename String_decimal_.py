t = int(input())

while t:
    str = input()
    flag=1
    for i in range(0,len(str)):
        if str[i].isdigit() == False:
            flag=0
            break
    if flag:
        print("True")
    else:
        print("False")
    t=t-1