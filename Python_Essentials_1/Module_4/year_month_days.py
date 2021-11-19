# SCENARIO
# Your task is to write and test a function which takes
# two arguments (a year and a month) and returns the number
# of days for the given month/year pair (while only February
# is sensitive to the year value, your function should be universal).

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


test_years = [1900, 2000, 2016, 1987, 1987]
test_months = [2, 2, 1, 11, 15]
test_results = [28, 29, 31, 30, None]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")