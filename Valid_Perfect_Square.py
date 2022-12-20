import math
def check(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        print("True")
    else:
        print("False")

t = int(input())

while(t):
    n = int(input())
    check(n)
    t=t-1