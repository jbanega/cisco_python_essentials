my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
final_list = []

for number in my_list:
    if number not in final_list:
        final_list.append(number)

my_list = final_list

print("The list with unique elements only:")
print(my_list)