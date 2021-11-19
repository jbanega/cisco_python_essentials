# COLLATZ IDEA
# In 1937, a German mathematician named Lothar Collatz
# formulated an intriguing hypothesis (it still remains unproven)
# which can be described in the following way:
# 
# 1) Take any non-negative and non-zero integer number and name it c0;
# 2) if it's even, evaluate a new c0 as c0 ÷ 2;
# 3) otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# 4) if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, 
# it will always go to 1.

c0 = int(input("Enter a integer number: "))
counter = 0

while (c0 != 1):
    if (c0 % 2 == 0):
        c0 = int(c0 / 2)
    else:
        c0 = int((3 * c0) + 1)
    counter += 1
    print(c0)
    if c0 == 1:
        break
print("steps =", counter)