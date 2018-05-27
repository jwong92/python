import sys

# this is how you create a function
# sumNum is not available outside the function of addNumber
def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum

print(addNumber(1,4))

# get user value, by using the system library and the objects inside to get a users input
print("What is your name?")
name = sys.stdin.readline()
print("Hello", name)

# More on string
long_string = "this is a longer string so we can test is"
# print first four letters
print(long_string[0:4])
# print the last 5 letters
print(long_string[-5:])
#print everything up to the last 5 letters
print(long_string[:-5])
# join two strings together using a substring
print(long_string[:4]+" be there")
# want to do formatting with strings
# %c = character, %s = string, $d = digit, %f = float (we say 5 decimal places)
print("%c is my %s letter and my number %d number is %.5f" %('X','favorite',10, .14))

print(long_string.capitalize()) # capitalize the firt letter of string
print(long_string.find("string")) # case sensitive - find index of where it is
print(long_string.isalnum()) # is the string all numbers? bool
print(long_string.isalpha()) # is the string all alphanumeric? bool
print(len(long_string)) # get the length of a string
print(long_string.replace("string", "Ground")) # replace a word in string
print(long_string.strip()) # strip any whitespace
quote_list = long_string.split(" ")
print(quote_list)