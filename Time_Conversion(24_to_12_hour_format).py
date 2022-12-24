hh, mm = input().split(":")
hh=int(hh)
mm=int(mm)
if hh>0 and hh<12:
    ampm='AM'
    print("{:02d}:{:02d} {}".format(hh,mm,ampm))
elif hh==0:
    hh=12
    ampm="AM"
    print("{:02d}:{:02d} {}".format(hh,mm,ampm))
elif hh==12:
    ampm="PM"
    print("{:02d}:{:02d} {}".format(hh,mm,ampm))
else:
    ampm="PM"
    hh=hh-12
    print("{:02d}:{:02d} {}".format(hh,mm,ampm))