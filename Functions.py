# Functions in Python
# Like in maths, where a function takes an argument and produces a result, it does so in python as well

# General form of Python function is:

# def function_name (arguments):
#   {lines telling the function what to do to produce the result}
#   return result

# Consider producing a function that returns 'x^2 + y^2'
def squared (x, y):
    result = x**2 + y**2
    return result

print(squared(10, 4))

# A new function
def born (country):
    return print ("I am from " + country)

born("Malawi")