import calendar

# Display calendar of a year
print(calendar.calendar(2021, w=2, l=1, c=6, m=3))
# Alternative prcal()
calendar.prcal(1998, m=6)


# Calendar for specific month
print(calendar.month(2020, 11))
# Alternative prmonth()
calendar.prmonth(2021, 12)


# The setfirstweekday() function
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)


# The weekday() function
print(calendar.weekday(2020, 12, 24))


# The weekheader() function
print(calendar.weekheader(3))


# Check leap year
print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))


# Calendar class
c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")
print()


# The itermonthdates() method
c = calendar.Calendar()

for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
print("\n")

# The itermonthdays() method (and its variants)
for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")
print("\n")

for iter in c.itermonthdays2(2019, 11):
    print(iter, end=" ")
print("\n")

for iter in c.itermonthdays3(2019, 11):
    print(iter, end=" ")
print("\n")

for iter in c.itermonthdays4(2019, 11):
    print(iter, end=" ")
print("\n")


# The monthdays2calendar() method
for data in c.monthdays2calendar(2020, 12):
    print(data)