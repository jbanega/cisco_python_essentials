# LAB: Evaluating student's result
# 
# Prof. Jekyll conducts classes with students and regularly makes
# notes in a text file. Each line of the file contains three elements: 
# the student's first name, the student's last name, and the number of
# point the student received during certain classes. The elements are
# separated with white spaces. Each student may appear more than once
# inside Prof. Jekyll's file.

# Task. Write a program which:
# 1) Asks the user for Prof. Jekyll's file name.
# 2) Reads the file contents and counts the sum of the received points
# for each student.
# 3) Prints a simple (but sorted) report.
# 4) The program must be fully protected against all possible failures:
# the file's non-existence, the file's emptiness, or any input data failures;
# encountering any data error should cause immediate program termination, 
# and the erroneous should be presented to the user.
# 5) Implement and use your own exceptions hierarchy.
# 6) Use a dictionary to store the students' data.


from os import strerror

# Defining exceptions
class StudentDataException(Exception):
    pass

class BadLine(StudentDataException):
    def __init__(self, line=0, message=""):
        StudentDataException.__init__(self, message)
        self.line = line

class FileEmpty(StudentDataException):
    def __init__(self, line=0, message=""):
        StudentDataException.__init__(self, message)
        self.line = line


def read_student_information(source_file_obj):
    global counter_lines
    student_info_by_line = source_file_obj.readline().split()

    if (counter_lines == 0) and (student_info_by_line == []):
        raise FileEmpty(counter_lines, "No information in the file")
    if (len(student_info_by_line) != 3) and (student_info_by_line != []):
        raise BadLine(counter_lines, "Incorrect elements by line")

    if (counter_lines != 0) and (student_info_by_line == []):
        pass

    counter_lines += 1
    return student_info_by_line


# Reading information
source = input("Enter the student's note file name: ")

try:
    handler = open(source, "rt")
    counter_lines = 0
except IOError as e:
    print("The file could not be opened:", strerror(e.errno))
    exit(e.errno)

students_data = {}

try:
    student_note = read_student_information(handler)
    while student_note != []:
        name = student_note[0] + " " + student_note[1]
        grade = float(student_note[2])
        if name not in students_data.keys():
            students_data[name] = grade
        else:
            students_data[name] += grade
        student_note = read_student_information(handler)

except FileEmpty as fe:
    print(fe)
    exit()
except BadLine as bad:
    print(bad, "- Check line", bad.line + 1)
    exit()
except ValueError as ve:
    print(ve, "Grade must be numeric. Check line", counter_lines)
    exit()
except:
    print("Sorry. An error ocurred during the process.")
    exit()

handler.close()

# Pritting the result
for key in sorted(students_data.keys()):
    print(f"{key:16s} {students_data[key]}")