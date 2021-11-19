# SCENARIO
# Your task is to write and test a function which takes
# one argument (a year) and returns True if the year is
# a leap year, or False otherwise.

def is_year_leap(year):
    if (year % 4 != 0):
        return False
    elif (year % 100 != 0):
        return True
    elif (year % 400 != 0):
        return False
    else:
        return True

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")