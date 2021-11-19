from datetime import datetime, date, time
import time as tm

# Date formatting
d = date(2020, 1, 4)
print(d.strftime("%Y/%m/%d"))

# Time formatting
t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d - %A - %H:%M:%S"))


# Using time module
timestamp = 1572879180
st = tm.gmtime(timestamp)

print(tm.strftime("%Y/%m/%d %H:%M:%S", st))
print(tm.strftime("%Y/%m/%d %H:%M:%S"))


# The strptime() function
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))
print(tm.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))