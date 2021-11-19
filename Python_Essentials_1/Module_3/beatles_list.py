# Step 1
beatles = []
print("Step 1:", beatles)

# Step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Step 3
for i in range(2):
    beatles.append(input("Add the following Beatles member [Stu Sutcliffe and Pete Best]: "))
print("Step 3:", beatles)

# Step 4
del beatles[3:]
print("Step 4:", beatles)

# Step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Testing list legth
print("The Fab", len(beatles))