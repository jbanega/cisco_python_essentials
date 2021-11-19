my_list = [8, 10, 6, 2, 4]
print("List to sort:", my_list) 
swapped = True  # We need it to enter the while loop.

while swapped:
    swapped = False  # no swaps so far
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # a swap occurred!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

print("Sorted list:", my_list)