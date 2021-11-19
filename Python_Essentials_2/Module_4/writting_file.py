from os import strerror

try:
	fo = open("newtext.txt", "wt")
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		fo.write(s)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))