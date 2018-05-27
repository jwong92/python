# if statements execute if condition is met, and whitespace groups blocks of code in python in a variety of ways

age = 21

# if age is greater than 16, will print
if age > 16 :
    print('You are old enough to drive')
else :
    print("You are not old enough to drive")

# use elif for multuple conditions
if age >= 21 :
    print("You are old enough to drive a tractor trailor")
elif age >= 16 :
    print("You are old enough to drive a car")
else :
    print("You are not old enough to drive")

# combine contiions with logical operators - and, or, not

if((age >= 1) and (age <= 18)) :
    print("you get a birthday")
elif (age == 21 or age >= 65) :
    print("you get a birthday")
elif not(age==30) :
    print("You don't get a birthday")
else :
    print("you get a birthday party yeah!")

