income = float(input("Enter the annual income: "))

thalers_reference = 85528.0

if income <= thalers_reference:
    tax = 0.18*income - 556.2
    if tax < 0:
        tax = 0.0
elif income > thalers_reference:
    tax = 14839.2 + 0.32*(income - thalers_reference)
else:
    tax = 0.0


tax = round(tax, 0)
print("The tax is:", tax, "thalers")