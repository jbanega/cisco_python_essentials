# THE TIMER CLASS

# The class will be called Timer. Its constructor accepts
# three arguments representing hours (a value from range [0..23]
# - it will be using the military time), minutes (from range [0..59])
# and seconds (from range [0..59]). 
# Zero is the default value for all of the above parameters.

# The class itself should provide the following facilities:
# 1) Objects of the class should be "printable", i.e. they should be
# able to implicitly convert themselves into strings of the following
# form: "hh:mm:ss", with leading zeros added when any of the values is
# less than 10.
# 2) The class should be equipped with parameterless methods called
# next_second() and previous_second(), incrementing the time stored inside
# objects by +1/-1 second respectively.
# 3) All object's properties should be private.

def formatting_time(hours=0, minutes=0, seconds=0):
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        # Running input validation
        assert (hours >= 0) and (hours <= 23), f"The entered hours ({hours}) are invalid. " \
            + "Must be a value from range [0, 23]"
        assert (minutes >= 0) and (minutes <= 59), f"The entered minutes ({minutes}) are invalid. " \
            + "Must be a value from range [0, 59]"
        assert (seconds >= 0) and (seconds <= 59), f"The entered seconds ({seconds}) are invalid. " \
            + "Must be a value from range [0, 59]"

        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return formatting_time(self.__hours, self.__minutes, self.__seconds)

    def next_second(self):
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self.__hours == 23:
                    self.__hours = 0
                else:
                    self.__hours +=1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1


    def prev_second(self):
        if self.__seconds == 0:
            self.__seconds = 59
            if self.__minutes == 0:
                self.__minutes = 59
                if self.__hours == 0:
                    self.__hours = 23
                else:
                    self.__hours -=1
            else:
                self.__minutes -= 1
        else:
            self.__seconds -= 1


# Testing class
timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)