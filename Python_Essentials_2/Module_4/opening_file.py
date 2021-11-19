# stream = open(file, mode = 'r', encoding = None)
try:
    stream = open("/Dir/file_name.txt", "rt")
    # Processing goes here.
    stream.close()
except Exception as exc:
    print("Cannot open the file:", exc)