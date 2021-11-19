# SCENARIO
# Your task is to write and test a function which takes
# three arguments (a year, a month, and a day of the month)
# and returns the corresponding day of the year, or returns
# None if any of the arguments is invalid.

def is_year_leap(year):
    if (year % 4 != 0):
        return False
    elif (year % 100 != 0):
        return True
    elif (year % 400 != 0):
        return False
    else:
        return True

def days_in_month(year, month):
    if (month < 0) or (month > 12):
        return
    year_leap = is_year_leap(year)
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year_leap:
        days_per_month[1] = 29
    days_in_selected_month = days_per_month[month - 1]
    return days_in_selected_month


def day_of_year(year, month, day):
    number_of_days_in_month = days_in_month(year, month)
    if day > number_of_days_in_month:
        return
    return str(day) + "/" + str(month) + "/" + str(year)


print(day_of_year(2000, 12, 31))


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_days = [29, 29, 31, 34]
test_results = [None, "29/2/2000", "31/1/2016", None]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    d = test_days[i]
    print(yr, mo, d, "-> ", end="")
    result = day_of_year(yr, mo, d)
    if result == test_results[i]:
	    print("OK")
    else:
	    print("Failed")