# LAB: Sorted character frequency histogram

# Task:
# 1) The output histogram will be sorted based on the characters'
# frequency (the bigger counter should be presented first).
# 2) The histogram should be sent to a file with the same name as
# the input one, but with the suffix '.hist' (it should be concatenated
# to the original name).


from os import strerror

source = input("Write the source file: ")

# Opening the file
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

# Writting the file
try:
    stream = open(source + ".hist", "wt")
except IOError as e:
    print("I/O error ocurred:", strerror(e.errno))
    exit(e.errno)

sorted_data = sorted(character_histogram.items(), key=lambda item: item[1], reverse=True)
for char, counter in sorted_data:
    info = f"{char} -> {counter}" 
    stream.write(info + "\n")
    print(info)

stream.close()