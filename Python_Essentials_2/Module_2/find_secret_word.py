# FIND A WORD GAME

# Let's play a game. We will give you two strings: one being a word 
# and the second being a combination of any characters.
# Task. Write a program which answers the following question: 
# are the characters comprising the first string hidden inside the second string?

# Test.
# test_data = [("donor", "Nabucodonosor"), ("donut", "Nabucodonosor")]
# expected_output = ["Yes", "No"]


def hidden_word(word: str, text: str):
    word = word.lower()
    text = text.lower()

    searched_word = ""
    pos = 0
    for n in word:
        index = text.find(n, pos)
        if index != -1:
            searched_word += text[index]
            pos = index
        else:
            print("No")
            return
    else:
        print("Yes")
        return


if __name__ == "__main__":
    test_data = [
        ("dog", "vcxzxduybfdsobywuefgas"),
        ("dog", "vcxzxdcybfdstbywuefsas"),
        ("donor", "Nabucodonosor"),
        ("donut", "Nabucodonosor")
        ]
    for sample in test_data:
        word, text = sample
        print(word, text, " -> ", end="")
        hidden_word(word, text)