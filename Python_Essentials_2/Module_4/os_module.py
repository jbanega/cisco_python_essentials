import os

print(os.name)

# Creating directory
os.mkdir("my_dir")
for n in os.listdir():
    print(n, end="\t")

# Recursive directory creation
os.makedirs("first_dir/second_dir")
os.chdir("first_dir")
print(os.listdir())
print(os.getcwd())

# Deleting directory
os.chdir("../")
os.rmdir("my_dir")

# Recursive directory delete
os.removedirs("first_dir/second_dir")

# System function (exit status 0 -> success)
returned_value = os.system("ipconfig")
print(returned_value)