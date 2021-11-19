from datetime import date, time, datetime
import time as tm


# Get current local date
today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


# Create a date object
my_date = date(2019, 11, 4)
print("My date:", my_date)


# Date object from timestamp
# Number of seconds from January 1, 1970 to the current moment
timestamp = tm.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)


# Date object using the ISO 8601 format (YYYY-MM-DD)
d = date.fromisoformat("2019-11-04")
print(d)


# The replace() method
d = date(1991, 2, 5)
print(d)

d = d.replace(year=1992, month=1, day=16)
print(d)

# Day of the week
d = date(2019, 11, 4)

week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
    }

weekday = week[d.weekday()]
print("Day:", d, "| Day of the week:", weekday)

# The isoweekday() method - ISO 85601 specification
iso_week = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
    }

iso_weekday = iso_week[d.isoweekday()]
print("Day:", d, "| Day of the week:", iso_weekday)


# Creating time objects
# time(hour, minute, second, microsecond, tzinfo, fold)
t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)


# The ctime() function
timestamp = 1572879180
print(tm.ctime(timestamp))
print(tm.ctime())


# The gmtime() and localtime() functions
timestamp = 1572879180
print(tm.gmtime(timestamp))     # struct_time object in UTC format
print(tm.localtime(timestamp))  # struct_time object in local time format


# The asctime() and mktime() functions
timestamp = 1572879180
st = tm.gmtime(timestamp)

# Convert struct_time object or tuple to string
print(tm.asctime(st))

# Convert struct_time object or tuple to the number of seconds since the Unix epoch
print(tm.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))


# Creating datetime objects
# datetime(year, month, day, hour, minute, second, microsecond, tzinfo, fold)
dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())

# Get current date and time
print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())

# Getting timestamp from datetime
dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())