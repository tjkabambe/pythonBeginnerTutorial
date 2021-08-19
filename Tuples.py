# Tuples in python

# Tuples are a sequence of items of any type but cannot be modified (Unlike lists)

# Tuples look like this
Fruit = ("Apple", 4, "Bananas", 5, "Oranges", 6)
print(type(Fruit))
# Tuples use '()' while lists use '[]'

list_of_fruit = ["Apple", 4, "Bananas", 5, "Oranges", 6]
print(type(list_of_fruit))

# We can modify lists
list_of_fruit[0] = "Strawberies"
print(list_of_fruit)

# We can't modify Tuples
# Fruit[0] = "Berries"
# print(Fruit)
# this will cause an error

# We can perform similar operations on tuples as with lists

# Slicing Tuples
print(Fruit[2:4])

# Recalling elements within a tuple
print(Fruit[0])

# Concatenation of tuples
Fruit = Fruit[0:4] + ("Cherries", 10)
print(Fruit)

# Tuples with one element must have a comma
x = (8, )
print(type(x))

# Find length of tuple
print(len(Fruit))

# Creating a tuple. must have double '()'
another_tuple = tuple(("hello", 18, True))
print(type(another_tuple))

# Converting a tuple to a list and back to a tuple
Fruit = list(Fruit)
Fruit.append("Grapes")
print (Fruit)
Fruit = tuple(Fruit)
print (Fruit)

# Unpacking tuples
Fruit = ("Apples", "Bananas", "Pears", "Strawberries", "Oranges")
(one, two, *three) = Fruit # * assings all the other elements other than the ones that have no assignments
print(one)
print(two)
print(three)

# Incorporate loops withing tuples
for i in range(len(Fruit)):
    print(Fruit[i])
