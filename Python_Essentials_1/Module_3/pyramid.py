blocks = int(input("Enter the number of blocks: "))
height = 0
blocks_to_use = 1

while blocks > 0:
        blocks -= blocks_to_use
        if blocks >= 0:
            height += 1
            blocks_to_use += 1
        else:
            break

print("The height of the pyramid:", height)