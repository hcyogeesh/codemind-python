tt,ampm=input().split()
hh,mm=tt.split(":")
hh=int(hh)
mm=int(mm)
if (ampm=='AM' and hh==12):
    print("00:00")
elif ampm=='PM' and hh==12:
    
    print("{:02d}:{:02d}".format(hh,mm))
elif ampm=='PM':
    hh=hh+12
    print("{:02d}:{:02d}".format(hh,mm))
else:
    print("{:02d}:{:02d}".format(hh,mm))

