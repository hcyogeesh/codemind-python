def fact(num):
    factorial = 1
    
    if num < 0:
       return -1
    elif num == 0:
       return 1
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       return factorial

t= int(input())
while(t):
    num=int(input())
    print(fact(num))
    t=t-1