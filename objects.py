import random
import sys
import os

# model real world things using code
# define attributes using variables inside class
# define abilities using functions

# class is a blueprint for creating an animal in this case
class Animal:
    # create attributes
    # these attributes are private, denoted by the double underscores. To change values or get them, have to use functions inside the class
    __name = None # can also be empty quotes
    __height = 0
    __weight = 0
    __sound = 0

    # constructors intialize an object with things to be passing in
    def __init__(self, name, height, weight, sound):
        # then we will define the properties by assigning them values
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

# self allows an object to refer itself inside of the class - when you create a class animals
# use encapsulation to get and set values, which means that you check to see if the variables are valid first before
    def set_name(self, name) :
        self.__name = name
    
    def get_name(self):
        return self.__name

    def set_height(self, height) :
        self.__height = height
    
    def get_height(self):
        return self.__height

    def set_weight(self, weight) :
        self.__weight = weight
    
    def get_weight(self):
        return self.__weight

    def set_sound(self, sound) :
        self.__sound = sound
    
    def get_sound(self):
        return self.__sound

# polymorphism
    def get_type(self):
        print("Animal") #print the object name

# because you're  in the class, don't need getters and setters to refer to the values in order to use them
# can use {} to use as a placeholder for values
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} His owner is".format(self.__name, self.__height, self.__weight, self.__sound)


cat = Animal("Whiskers", 33, 10, 'Meow')
print(cat.toString())


# Inheritance
# get all variables and functions in the animal class
class Dog(Animal) :
    # attributes defined in here are strictly found in this class, and not in others outside it. All dogs will have an owner, but not all animals will have an owner
    __owner = ""

    # constructor here with parameters that are the same as the extended class
    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        # create another constructor, but using the attributes from the previous class, so 
        # Create a super class
        super(Dog, self).__init__(name, height, weight, sound)

# allow them to set /get the owner
    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

# define the get type 
    def get_type(self):
        print("Dog")

# can override the functions in super class by creating a function with the same name in the super class
    def toString(self):
        return "{} is {} cm tall and {} kilograms and say {} His owner is {}".format(self.__name, self.__height, self.__weight, self.__sound, self.__owner)
# Method overloading
# Perform different tasks based off the attributes that are sent in

# make it ok for them not to set an attribute of how_many (by setting to none)
# want to give them the option to send in the number of barks a dog makes

    def multiple_sounds(self, how_many = None):
        if how_many is None: 
            print(self.get_sound())
        else: # if they pass in a value, print the number of times they say 
            print(self.get_sound() * how_many)

spot = Dog("Spot", 53, 21, "Ruff", "Jessica")
# call the function toString
print(spot.toString())