# Incorporating the if statement with a boolean
x = 10
y = 4

if x % y == 0:
    print (True)
else:
    print (False)

# While loop
number = 1
while number < 4:
    print (number)
    if number == 4:
        break
    number = number + 1

# Incorporating the else statement in the while loop

number = 2
while number < 4:
    print (number)
    number = number + 1
else:
    print ("number is no longer less than 4")


# If statement
number = 3
if number > 0:
    print ("Positive Number")
elif number == 0:
    print ("Zero")
else:
    print ("Negative Number")