n = int(input())
lst = list(map(int, input().split()))
sum = sum(lst)
avg = sum/n
print("{:.2f}".format(avg))