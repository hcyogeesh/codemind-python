import math
def is_prime(n):
    if n <= 1:          # negative numbers, 0 or 1
        return False
    if n <= 3:          # 2 and 3
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

m=int(input())
n=int(input())
count=0
for i in range(m, n+1):
    if is_prime(i):
        count+=1

print(count)