import os

# create AND open a file open(name of the file, file permissions)
# wb = write
# ab+ = to read and append to file = also opens/creates the file
test_file = open("test.txt", "wb")

# print file mode which is wb
print(test_file.mode)

# print file name
print(test_file.name)

# write text to screen or file
test_file.write(bytes("Write me to the file \n", 'UTF-8'))

# close a file
test_file.close()

# READING information
# want to open for reading and writing, r+
test_file = open('test.txt', 'r+')
text_in_file = test_file.read()
print(text_in_file)

# DELETE the file using the OS module
os.remove("test.txt")