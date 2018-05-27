# You can import a number of modules using
# for importing random numbers
import random 
import sys
import os

print("Hello World")

'''
multiline comment
'''

# variables store values and can't begin with number
name = "Derek"
print(name)

# 5 main datatypes
    # numbers
    # string
    # lists
    # tuples
    # dictionaries (lists)

# Can add commas in print, to hold more than one value
print("1 + 2 - 3 * 2 =", 1 + 2 - 3 * 2)

quote = "\"Always remember you are unique"
multi_line_quote = ''' just like everyone 
else '''

# join two strings - use %s in print to declare spaces
new_string = quote + multi_line_quote
print("%s %s %s" %('I like the quote', quote, multi_line_quote))

# print 5 new lines
print('\n' * 5)

# print to screen without havng a new line each time you print
print("I don't like this ", end="")
print("newlines")

# LISTS

grocery_list = ['juice', 'tomatoes', 'potatoes', 
                'bananas']

# print the first item in the list
print('First Item', grocery_list[0])

# change value in list
grocery_list[0] = "Green Juice"

# print items from list
print(grocery_list[1:3]) # prints up until 3, not includes

# add lists in lists
other_events = ['wash car', 'pick up kids', 'cash check']

to_do_list = [other_events, grocery_list]
print("To do list:", to_do_list)

# want the second item out of the second list
print((to_do_list[1][1]))

# append items
grocery_list.append("Onions")

# Want to insert item into specific order
grocery_list.insert(1, "Pickle")

# remove frrom the list
grocery_list.remove("Pickle")

# sort the list
grocery_list.sort()

# reverse the list
grocery_list.reverse()

del grocery_list[4]
print(to_do_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
# what comes last
print(max(to_do_list2))
# what comes in first alphabetically
print(min(to_do_list2))