# SITUATION
# It's a huge hotel consisting of three buildings,
# 15 floors each. There are 20 rooms on each floor.
# For this, you need an array which can collect and
# process information on the occupied/free rooms

rooms = [[[False for room in range(20)] for floor in range(15)] for building in range(3)]
# for building in rooms:
#     print(building)

# Book a room (second building, on the tenth floor, room 14)
rooms[1][9][13] = True

# Release a room (second room on the fifth floor located in the first building)
rooms[0][4][1] = False

# Check vacancies (15th floor of the third building)
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1