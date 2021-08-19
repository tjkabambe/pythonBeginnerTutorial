# Strings

# Int, floats and booleans are considered simple, ie cannot be broken down

# Lists and strings are made up of smaller peaces which CAN be broken down

# Type
print("hello world")
print(type("hello world"))

# Operations on strings

# Addition sign Concantenation
Greeting = "Hello "
Name = "Trevor"
print(Greeting + Name)

# * Operator
print(Name*3)
print(Greeting + Name*3)

# Index Operator
Name = "Ellie"
print(Name[4] + Name[1])

# Slicing strings
print(Name[0:3])
print(Name[:3])
print(Name[2:])

# Lowercase and Uppercase
Name = "Trevor"
print(Name.lower())
print(Name.upper())

# Count how many times a character appears in a string
print(Name.count("r"))

# Replace specific characters with other characters
print(Name.replace("o", "a"))
New_Name = Name.replace("r", "l")
print (New_Name)

# Find length of the string
print(len(Name))

# Format strings
# your_name = input("Your name: ")
# hello = "Hello {}".format(your_name)
# print(hello)

# Each letter in python is assigned to a specific number
print("orange" < "strawberry")
print(ord("o"))
print(chr(108))
# We can perform maths on strings

# In and not operators
fruit = "Banana"
print("a" in fruit)
print("s" not in fruit)

# Incorporate a few things we've learnt so far
x = "hello"
y = ""
for character in x:
    y = character.upper() + y
print(y)