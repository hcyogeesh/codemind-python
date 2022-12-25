h,sn,sp=map(int, input().split())

if (h>50 and sn>=60 and sp>100):
    grade=10
elif (h>50 and sn>=60):
    grade =9
elif (sn>=60 and sp>100):
    grade=8
elif (h>50 and sp>100):
    grade=7
elif (h>50 or sn>=60 or sp>100):
    grade =6
else:
    grade=5

print(grade)