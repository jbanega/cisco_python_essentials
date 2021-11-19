# LAB: Searching for directory

# Write a program that will search for directories in a given location.
# Requeriments:
# 1) Write a function or method called find that takes two arguments
# called path and dir. The path argument should accept a relative or absolute
# path to a directory where the search should start, while the dir argument
# should be the name of a directory that you want to find in the given path.
# Your program should display the absolute paths if it finds a directory with
# the given name.
# 2) The directory search should be done recursively. This means that the search
# should also include all subdirectories in the given path.

import os

def find(path, dir):
    os.chdir(path)
    content = os.listdir()
    if dir in content:
        os.chdir(dir)
        print(os.getcwd(), "\n")
        os.chdir("../")
    for element in content:
        find(element, dir)
        os.chdir("../")

find(path="./tree", dir="python")