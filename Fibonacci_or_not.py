def checkFib(n):
    
    a = 0
    b = 1
    while a <= n:
        if n == a:
            return True
        a, b = b, a + b
    
    return False

n = int(input())
if checkFib(n):
    print("True")
else:
        print("False")