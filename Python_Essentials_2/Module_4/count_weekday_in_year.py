# LAB: Count weekday in year

# Task. To extend the Calendar class functionality with a
# new method called count_weekday_in_year, which takes a year
# and a weekday as parameters, and then returns the number of
# occurrences of a specific weekday in the year.

# Tips:
# 1) Create a class called MyCalendar that extends the Calendar class.
# 2) Create the count_weekday_in_year method with the year and
# weekday parameters. The weekday parameter should be a value between
# 0-6, where 0 is Monday and 6 is Sunday. The method should return the
# number of days as an integer.
# 3) Use the monthdays2calendar method of the Calendar class.

# Sample test:
# year=2019, weekday=0 -> output: 52
# year=2000, weekday=6 -> output: 53


from calendar import Calendar

class MyCalendar(Calendar):
    def __init__(self):
        super().__init__()

    def count_weekday_in_year(self, year: int, weekday: int):
        count_weekday = 0
        for month in range(1, 13):
            weeks_in_month = self.monthdays2calendar(year, month)
            for week in weeks_in_month:
                for number_day, w_day in week:
                    if (number_day != 0) and (weekday == w_day):
                        count_weekday += 1
                    else:
                        continue
        return count_weekday

my_cal = MyCalendar()
print(my_cal.count_weekday_in_year(year=2019, weekday=0))
print(my_cal.count_weekday_in_year(year=2000, weekday=6))