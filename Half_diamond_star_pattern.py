def pattern(n):
    if n<3:
        print("The pattern is not possible")
        return
    for i in range(0, n):
        for j in range(0, i+1):
            print("*", end="")
        print()
    for i in range(n-1, 0 , -1):
        for j in range(0, i):
            print("*", end="")
        print()

n=int(input())
pattern(n)