# THE DAY OF THE WEEK

# The task is to implement a class called Weeker.
# This class will be able to store and to manipulate days of a week.
# The class constructor accepts one argument - a string. The string
# represents the name of the day of the week and the only acceptable
# values must come from the following set:
# Mon Tue Wed Thu Fri Sat Sun
# Invoking the constructor with an argument from outside this set should
# raise the WeekDayError exception.

# The class should provide the following facilities:
# 1) Objects of the class should be "printable", i.e. they should be able
# to implicitly convert themselves into strings of the same form as the
# constructor arguments.
# 2) The class should be equipped with one-parameter methods called add_days(n)
# and subtract_days(n), with n being an integer number and updating the day of
# week stored inside the object in the way reflecting the change of date by the
# indicated number of days, forward or backward.
# 3) All object's properties should be private.

class WeekDayError(Exception):
    pass
	

class Weeker:
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        try:
            self.__index = Weeker.days_of_week.index(day)
        except:
            # print(f"The entered day must be one of the following {Weeker.days_of_week}.")
            raise WeekDayError
        self.__day = Weeker.days_of_week[self.__index]

    def __str__(self):
        return self.__day

    def add_days(self, n):
        while (self.__index + n) > (len(Weeker.days_of_week) - 1):
            n = (self.__index + n) - len(Weeker.days_of_week)
            self.__index = 0
        else:
            self.__index += n
        self.__day = Weeker.days_of_week[self.__index]

    def subtract_days(self, n):
        while (self.__index - n) < 0:
            n = n - self.__index
            self.__index = len(Weeker.days_of_week)
        if n > 0:
            self.__index -= n
        self.__day = Weeker.days_of_week[self.__index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")