# GENERATOR TO PRODUCE THE FIRST n POWERS OF 2

def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)

# List comprehension
print()
t = [x for x in powers_of_2(5)]
print(t)

# List function
print()
lfunc = list(powers_of_2(3))
print(lfunc)