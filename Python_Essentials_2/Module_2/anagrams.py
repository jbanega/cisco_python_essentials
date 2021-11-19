# ANAGRAMS
# An anagram is a new word formed by rearranging the letters
# of a word, using all the original letters exactly once.

# Task: write a program which:
# - Asks the user for two separate texts.
# - Checks whether, the entered texts are anagrams and prints the result.

# Assumptions:
# - Two empty strings are not anagrams.
# - Upper and lower-case letters are treated as equal.
# - Spaces are not taken into account during the check. They are
# treated as non-existent.

# Test:
# test_data = [("Listen", "Silent"), ("modern", "norman")]
# expected_output = ["Anagrams", "Not anagrams"]

def are_anagrams():
    first_text = input("Enter the first text: ")
    second_text = input("Enter the second text: ")

    if (first_text == "") or (second_text == ""):
        print("You must enter two texts.")
        return

    words_of_first_text = first_text.upper().split()
    words_of_second_text = second_text.upper().split()

    letters_of_text_1 = sorted("".join(words_of_first_text))
    letters_of_text_2 = sorted("".join(words_of_second_text))

    if len(letters_of_text_1) == len(letters_of_text_2):
        for n in range(len(letters_of_text_1)):
            if letters_of_text_1[n] == letters_of_text_2[n]:
                continue
            else:
                print("Not anagrams")
                return
        else:
            print("Anagrams")
            return
    else:
        print("Not anagrams")
        return


if __name__ == "__main__":
    are_anagrams()