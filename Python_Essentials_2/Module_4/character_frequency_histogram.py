# LAB: Character frequency histogram

# Task:
# 1) Asks the user for the input file's name.
# 2) Reads the file (if possible) and counts all the Latin letters
# (lower- and upper-case letters are treated as equal).
# 3) Prints a simple histogram in alphabetical order (only non-zero
# counts should be presented).


from os import strerror

source = input("Write the source file: ")

try:
    handler = open(source, "rt")
except IOError as e:
    print("I/O error ocurred:", strerror(e.errno))
    exit(e.errno)

character_histogram = {}
data = handler.read()
for char in data:
    if char.isspace():
        continue
    if char.isalpha():
        char = char.lower()
    else:
        continue
    if char not in character_histogram.keys():
        character_histogram[char] = 1
    else:
        character_histogram[char] += 1

handler.close()

for key in sorted(character_histogram.keys()):
    print(key, "->", character_histogram[key])