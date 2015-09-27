import datetime
for i in range(1006,1997,10):
    d = datetime.date(i,1,26)
    if i%4==0 and d.weekday()==0:
        print i
