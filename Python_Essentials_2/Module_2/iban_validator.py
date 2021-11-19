# IBAN Validator
# Algorithm used by European banks to specify account numbers.
# The standard named IBAN (International Bank Account Number)
# provides a simple and fairly reliable method of validating
# the account numbers against simple typos that can occur during
# rewriting of the number.

# An IBAN-compliant account number consists of:
# - Two-letter country code taken from the ISO 3166-1 standard
# (e.g., FR for France, GB for Great Britain, DE for Germany, and so on).
# - Two check digits used to perform the validity checks.
# - The actual account number (up to 30 alphanumeric characters.
# The length of that part depends on the country).

# The standard says that validation requires the following steps:
# (step 1) Check that the total IBAN length is correct as per the
# country (this program won't do that).
# (step 2) Move the four initial characters to the end of the string
# (i.e., the country code and the check digits).
# (step 3) Replace each letter in the string with two digits, thereby
# expanding the string, where A = 10, B = 11 ... Z = 35.
# (step 4) Interpret the string as a decimal integer and compute the
# remainder of that number on division by 97; If the remainder is 1,
# the check digit test is passed and the IBAN might be valid.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")


# Test data:
# British: GB72 HBZU 7006 7212 1253 00
# French: FR76 30003 03620 00020216907 50
# German: DE02100100100152517108