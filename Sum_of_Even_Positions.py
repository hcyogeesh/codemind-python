n = int(input())
lst = list(map(int, input().split()))
sum = 0
for i in lst:
    k = lst.index(i)
    if k%2==0:
        sum = sum + i
print(sum)