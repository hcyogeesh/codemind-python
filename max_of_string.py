max=0
str=input()
for i in range(0,len(str)):
    if ord(str[i])>max:
        max=ord(str[i])

print(chr(max))