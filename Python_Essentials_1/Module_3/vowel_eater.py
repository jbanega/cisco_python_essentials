print("VOWER EATER PROGRAM\n")
user_word = input("Enter a word: ")
user_word = user_word.upper()
word_without_vowels = ""

for letter in user_word:
    if (letter == "A"):
        continue
    elif (letter == "E"):
        continue
    elif (letter == "I"):
        continue
    elif (letter == "O"):
        continue
    elif (letter == "U"):
        continue
    else:
        print(letter)
        word_without_vowels += letter
print("Word without vowels:", word_without_vowels)