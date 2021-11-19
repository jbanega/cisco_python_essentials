# REFACTORED CAESAR CYPHER

# Assumptions:
# - Allow the shifted value to come from the range 1...25 inclusive.
# - Preserve the letters' case (lower-case letters will remain lower-case)
# and all non-alphabetical characters should remain untouched.

# Test
# test_data = [("abcxyzABCxyz 123", 2), ("The die is cast", 25)]
# expected_output = ["cdezabCDEzab 123", "Sgd chd hr bzrs"]

def cypher_message():
    text = input("Enter a message to encrypt: ")
    if text == "":
        print("No message to encrypt.")
        return
    shift_value = input("Enter a shift value [from 1 to 25]: ")
    if not shift_value.isnumeric():
        print("The shift value must be an integer number between 1 and 25.")
        return
    
    cypher = ""
    shift_value = int(shift_value)
    if (shift_value < 1) or (shift_value > 25):
        print("The shift value must be an integer number between 1 and 25.")
        return
        
    for character in text:

        if character.isalpha():
            code = ord(character)

            if character.isupper():
                var_z = "Z"
                var_a = "A"
            elif character.islower():
                var_z = "z"
                var_a = "a"

            if code == ord(var_z):
                code = ord(var_a) + (shift_value - 1)
            elif (code + shift_value) > ord(var_z):
                remaining = ord(var_z) - code
                code = ord(var_a) + (shift_value - remaining - 1)
            else:
                code += shift_value

            cypher += chr(code) 
        else:
            cypher += character
        
    print(cypher)
    return cypher


if __name__ == "__main__":
    cypher_message()