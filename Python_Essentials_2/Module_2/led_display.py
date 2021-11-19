# SCENARIO: LED display

# Task: to write a program which is able to simulate
# the work of a seven-display device, although you're
# going to use single LEDs instead of segments.
# Each digit is constructed from 13 LEDs.
# The code has to display any non-negative integer number
# entered by the user.

map_of_digits = [
"""
 ###
 # #
 # #
 # #
 ###
""",
"""
   #
   #
   #
   #
   #
""",
"""
 ###
   #
 ###
 #  
 ###
""",
"""
 ###
   #
 ###
   #
 ###
""",
"""
 # #
 # #
 ###
   #
   #
""",
"""
 ###
 #  
 ###
   #
 ###
""",
"""
 ###
 #  
 ###
 # #
 ###
""",
"""
 ###
   #
   #
   #
   #
""",
"""
 ###
 # #
 ###
 # #
 ###
""",
"""
 ###
 # #
 ###
   #
 ###
"""
]

def led_display():
    user_input = input("Enter any non-negative integer number: ")
    list_of_numbers_by_user_input = []
    for number in user_input:
        index = int(number)
        list_of_numbers_by_user_input.append(map_of_digits[index].split("\n"))

    display_result = ""
    for n in range(1, 6):
        for element in list_of_numbers_by_user_input:
            display_result += element[n]
        display_result += "\n"

    print("\n" + display_result)


if __name__ == "__main__":
    try:
        led_display()
    except:
        print("You must enter a non-negative integer number. Try again.")