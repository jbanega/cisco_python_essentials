# SCENARIO
# Task: to write your own function, which behaves almost
# exactly like the original split() method.
# - It should accept exactly one argument - a string.
# - It should return a list of words created from the
# string, divided in the places where the string contains
# whitespaces.
# - If the string is empty, the function should return an
# empty list.


def mysplit(strng):
    splitted_text = []
    word = ""
    for character in strng:
        if character != " ":
            word += character
        else:
            if word == "":
                continue
            splitted_text.append(word)
            word = ""
    else:
        if word != "":
            splitted_text.append(word)
    return splitted_text


if __name__ == "__main__":
    test_data = [
        "To be or not to be, that is the question",
        "To be or not to be,that is the question",
        "   ",
        " abc ",
        ""
    ]
    expected_output = [
        ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question'],
        ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question'],
        [],
        ['abc'],
        []
    ]

    for n, test in enumerate(test_data):
        result = mysplit(test)
        print(result, end="")
        if result == expected_output[n]:
            print(" -> OK")
        else:
            print(" -> Failed")