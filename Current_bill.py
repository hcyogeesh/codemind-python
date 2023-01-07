units = int(input())
if units<=199:
    bill=units*1.20
elif units<400:
    bill=units*1.50
elif units<600:
    bill = units*1.80
elif units>=600:
    bill = units*2.00

surcharge=0           
if bill>400:
    surcharge=bill*0.15
if bill<400:
    surcharge=100
    
bill=bill+surcharge
    
print("{:.2f}".format(bill))