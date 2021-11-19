secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

guess_number = int(input("Write an integer number: "))

while guess_number != secret_number:
    print("Ha ha! You're stuck in my loop!\n")
    guess_number = int(input("Write an integer number: "))
if guess_number == secret_number:
    print("Secret number:", secret_number)
    print("Well done, muggle! You are free now.")