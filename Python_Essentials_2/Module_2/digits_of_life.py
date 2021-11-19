# THE DIGIT OF LIFE

# The Digit of Life is a digit evaluated using somebody's birthday.
# It's simple - you just need to sum all the digits of the date.
# If the result contains more than one digit, you have to repeat the
# addition until you get exactly one digit.
# For example:
# 1 January 2017 = 2017 01 01
# 2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
# 1 + 2 = 3

# Task. Write a program which:
# - Asks the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM,
# or MMDDYYYY (the order of the digits doesn't matter).
# - Outputs the Digit of Life for the date.

# Test
# test_data = ["19991229", "20000101"]
# expected_output = [6, 4]


def digit_of_life():
    birthday = input("Enter the date of your birthday [YYYYMMDD]: ")
    if not birthday.isdigit():
        print("Enter a valid date.")
        return
    if len(birthday) != 8:
        print("Please check the format of the date and enter your birthday again.")
        return

    digit_of_life = birthday
    total = 0
    
    while len(digit_of_life) != 1:
        for n in digit_of_life:
            total += int(n)
        digit_of_life = str(total)
        total = 0
    
    print(digit_of_life)


if __name__ == "__main__":
    digit_of_life()