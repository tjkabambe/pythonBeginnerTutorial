# Python types

# Basic types in Python
print(type("Hello world"))  # string
print(type(12))  # integer
print(type(22.2))  # float
print(type(True))  # boolean

# Moving to integers
print(4.99, int(33.66))  # Python rounds down by default
print(2.11, int(2.55))

# Rounding up!
print(4.99, int(round(33.66)))  # 'round' rounds up!

# Moving string to integers
print("1234", int("1234"))  # If you want to move strings to integers, they must be numbers

# Moving to float
print(float(80))
print(float("1234"))

# Moving to Strings
print(str(12.3))
print(type(str(12.3)))

# Logical operators

# There are 3 diff. logical operators: 'and', 'or', 'not'
x = 6
print(x > 0 and x < 5)

y = 24
print(y % 2 == 0 or y % 5 == 0)

z = 2
print(z != 1)
