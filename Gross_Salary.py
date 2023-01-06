salary = int(input())

if salary<=10000:
    da=0.8
    hra=0.2
elif salary<=20000:
    da=0.9
    hra=0.25
elif salary>20000:
    da=0.95
    hra=0.30

gross = salary+salary*da+salary*hra

print("{:.2f}".format(gross))
