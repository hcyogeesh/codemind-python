rows=int(input())
ch='A'
for i in range(1, rows + 1):
    for j in range(1, rows+1):
        print(ch, end=" ")
    ch=chr(ord(ch)+1)
    print()