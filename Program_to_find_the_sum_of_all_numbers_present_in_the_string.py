sum=0
str=input()
for i in range(0,len(str)):
    if str[i].isdigit():
        sum=sum+int(str[i])

print(sum)