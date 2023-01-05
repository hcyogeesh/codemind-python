n=int(input())

if n>=800:
    rate=2
elif n>=600:
    rate = 1.8
elif n>=400:
    rate=1.6
elif n>=200:
    rate=1.4
else:
    rate=1.2

bill = n * rate

if bill>=400:
    sur = 0.15 * bill
else:
    sur = 0

totalamount = bill + sur
print("Units Consumed:",n)
print("Cost per Unit: {:.2f}".format(rate))
print("Bill: {:.2f}".format(bill))
print("Surcharge: {:.2f}".format(sur))
print("Total Amount: {:.2f}".format(totalamount))
