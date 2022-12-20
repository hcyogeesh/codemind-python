num = int(input())
sign=1
if num<0:
    sign=-1
    num=num*sign
reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

print(reversed_num*sign)