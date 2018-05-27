# You can import a number of modules using
# for importing random numbers
import random 
import sys
import os

# dictionaries made up of key value pairs, but dictionaries can't be joined with + signs
super_villains = {'Fiddler' : 'Issac Bowin',
                    'Captain Cold' : 'Leonard Snart',
                    'Weather Wizard' : 'Mark Mardon',
                    'Mirror Master' : 'Sam Scudder',
                    'Pied Piper' : 'Thomas Peterson'}

print(super_villains['Captain Cold'])

# delete the super villain
del super_villains['Fiddler']

# change the value
super_villains['Pied Piper'] = 'Hartley Rathaway'

# get the length of the value
print(len(super_villains))

# get the value by passing in a key
print(super_villains.get('Pied Piper'))

# get all the keys
print(super_villains.keys())

# get all values
print(super_villains.values())