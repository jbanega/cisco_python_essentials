# CAESAR CIPHER
# This cipher was (probably) invented and used by
# Gaius Julius Caesar and his troops during the
# Gallic Wars. The idea is rather simple - every letter
# of the message is replaced by its nearest consequent
# (A becomes B, B becomes C, and so on). The only exception
# is Z, which becomes A.

# Assumptions:
# - It accepts Latin letters only (note: the Romans used
# neither whitespaces nor digits).
# - All letters of the message are in upper case (note: 
# the Romans knew only capitals).

def encrypting_message():

    text = input("Enter your message: ")
    cipher = ''
    for char in text:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) + 1
        if code > ord('Z'):
            code = ord('A')
        cipher += chr(code)

    print(cipher)
    return cipher


# Decrypting a message

def decrypting_message(cipher):
    # cipher = input('Enter your cryptogram: ')
    text = ''
    for char in cipher:
        if not char.isalpha():
            continue
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
        text += chr(code)

    print(text)
    return text


if __name__ == "__main__":
    cipher = encrypting_message()
    decrypting_message(cipher)