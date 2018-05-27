# You can import a number of modules using
# for importing random numbers
import random 
import sys
import os


# FOR LOOPS
# work up to but not equal to 10
for x in range(1, 10):
    print(x, '', end="")

print('\n')

grocery_list = ['juice', 'tomatoes', 'potatoes', 'bananas']

for y in grocery_list:
    print(y)

# can define the number of cycles to list through
for x in [2,4,6,8,10]:
    print(x)

num_list = [[1,2,3],[10,20,30],[100,200,300]]

# nesting for loops
for x in range(0,3):
    for y in range(0,3):
        print(num_list[x][y])


# WHILE LOOPS

# in order to use some functions, you need to import libraries (for example, randrange is from the imported random library)
random_num = random.randrange(1,100)

# while random number is not 15, print the random number, and create a new random one
while(random_num != 15):
    print(random_num)
    random_num = random.randrange(1,100)

i = 0;
while(i<=20):
    if(i%2 == 0):
        print(i) # this will still continue the while loop
    elif(i==9):
        break # this will break out of the while loop
    else:
        i += 1
        continue
    i += 1