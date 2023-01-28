n = int(input())
lst = list(map(int, input().split()))
k = int(input())
for i in lst:
    if k==i:
        print("True")
        break
else:
    print("False")