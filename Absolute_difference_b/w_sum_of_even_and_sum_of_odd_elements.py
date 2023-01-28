n = int(input())
lst = list(map(int, input().split()))
sumodd = 0
sumeven=0
for i in lst:
    if i%2==0:
        sumeven = sumeven +i
    else:
        sumodd = sumodd +i
diff = abs(sumodd-sumeven)
print(diff)