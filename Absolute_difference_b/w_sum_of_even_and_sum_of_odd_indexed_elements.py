n = int(input())
lst = list(map(int, input().split()))
sumodd = 0
sumeven=0
for i in range(n):
    if i%2==0:
        sumeven = sumeven +lst[i]
    else:
        sumodd = sumodd +lst[i]
diff = abs(sumodd-sumeven)
print(diff)