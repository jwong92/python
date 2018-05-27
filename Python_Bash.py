# Google Python in Bash

# Begin by entering keyword 'python' or 'python3' into bash

a = 6
g = 10 + 3

# These are all valid assignments to variables. When you call a/g, it'll spit out the assignment
# Variables are case sensitive

a = "Hello"
len(a) # 5

a = 5
#len(a) will give you an error

# You can't add a string and number, but you can convert the number to a string

#a = "Hello" + 6 # CAN'T do this
a = "Hello" + str(6) # CAN do this

# to print command line arguements
# importing sys allows you to access these
# sys is a module
# use modules to help us write code
# in terminal type: python3, import sys, dir(sys) to see commands
# help(sys) also helps you
# can ask for specific instructions like help(len)
import sys


# defining another function called hello
def Hello(s):
    name = name + '!!!!!!!!!'
    print ("Hello", name)

# Typically main() contains the main function, and def is the syntax to declare a function
def main():
    print ("Hello")

    # in cli, you put letters, and it will be put into a list
    print (sys.argv)

# boiler plate that calls and runs the main() function
# python program can be run, which is true, and we say if it's true, then run the main function
# should always go to the bottom of script
if __name__ == '__main__':
    main()

# can load a python module (aka file) but don't want to run it - if that's the case, the if statement above is false.


