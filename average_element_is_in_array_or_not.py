n = int(input())
lst = list(map(int, input().split()))
sum  = sum(lst)
avg = int(sum/n)
for i in lst:
    if i==avg:
        print("True")
        break
else:
    print("False")
