# PALINDROMES
# Palindrome is a word which look the same when
# read forward and backward.
# Write a program which:
# - Asks the user for some text.
# - Checks whether the entered text is a palindrome,
# and prints result.

# Assumptions:
# - Empty string isn't a palindrome.
# - Upper and lower case letters are treated as equal.
# - Spaces are not taken into account during the check. 
# They are treated as non-existent.

# Test
# test_data = ["Ten animals I slam in a net", "Eleven animals I slam in a net"]
# expected_output = ["It's a palindrome", "It's not a palindrome"]

def is_palindrome():
    text = input("Enter a text: ")
    if text == "":
        print("No text. So It's not a palindrome.")
        return

    list_of_words = text.split()
    text_to_check = "".join(list_of_words).upper()

    for n in range(len(text_to_check)//2):
        if text_to_check[n] == text_to_check[-1 - n]:
            continue
        else:
            print("It's not a palindrome.")
            return
    else:
        print("It's a palindrome.")
        return


if __name__ == "__main__":
    is_palindrome()