n =int(input())
for i in range(n,0,-1):
    x=ord('A')+i-1
    for j in range(1,i+1):
        print(chr(x), end=" ")
    print()