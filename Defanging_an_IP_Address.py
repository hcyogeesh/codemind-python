str=input()

for i in range(0,len(str)):
    if str[i]=='.':
        print("[.]", end='')
    else:
        print(str[i], end='')
    