# Stream errors
from os import strerror
import errno

for err_number in sorted(errno.errorcode.keys()):
    print(err_number, errno.errorcode[err_number], ":", strerror(err_number))

print()


# Diagnosing stream problems
try:
    s = open("/Desktop/file.txt", "rt")
    # Actual processing goes here.
    s.close()
except Exception as exc:
    print("The file could not be opened:", strerror(exc.errno))