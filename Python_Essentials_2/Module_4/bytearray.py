from os import strerror


# Writting binary file
data = bytearray(10)
for i in range(len(data)):
    data[i] = 10 - i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# Reading binary file
data_to_read = bytearray(10)

try:
    bf = open('file.bin', 'rb')
    bf.readinto(data_to_read)
    bf.close()

    for b in data_to_read:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

print()


# Method 2 to reading binary files
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))