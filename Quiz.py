# Quiz time

# Question 1: Assigning variables
# create 2 variables x and y where any number you want
# find sum of x and y, x divided by y, x minus y, x multiplied by y
x = 4
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)

# Question 2: Lists
# Create a list of all even numbers from 0 to 100
# Print first 10 elements and find the length of this list
# Append a value of your choice to the end of the list (It can be any type!)
mylist = list(range(0, 101, 2))  # Create the list
print(mylist[0:10])  # Print the first 10 elements
print(len(mylist))  # Print length of list
mylist.append(102)  # Add element to list
print(mylist)

# Question 3
# Assign a variable to any integer you want
# using an if statement, find whether this integer is divisible by 5
# Get python to print whether it is or isn't
x = 19
if x % 5 == True:
    print("x is divisible by 5")
else:
    print("x is NOT divisible by 5")

# Question 4
# Using a for loop, get python to print the numbers 0 to 5
for i in range(6):
    print(i)

# Question 5
# Draw a pentagon in turtle
import turtle

for i in range(5):
    turtle.forward(150)
    turtle.left(72)
turtle.done()


# Question 6
# Create a function that tests whether three number (a,b,c) are a pythagorean triple
# ie if a^2 + b^2 = c^2

def pythagorean(a, b, c):
    if a ** 2 + b ** 2 == c ** 2:
        return print("These 3 numbers are pythagorean triple.")
    else:
        return print("These 3 numbers are not a pythagorean triple.")

print(pythagorean(3, 4, 5))  # this is true
print(pythagorean(1, 4, 9))  # this is false

# Question 7
# Spot the error
n = 5
while n < 10:
    n = n + 1
    print(n)

# Question 8
# Create 2 lists (of size 5) and plot these lists against each other using matplotlib
import matplotlib.pyplot as plt

list2 = [1, 3, 5, 8, 11, 16, 22]
list3 = [2, 4, 6, 8, 10, 12, 14]

plt.plot(list2, list3, c="blue", linewidth=2, Label="lines", linestyle="dashed")
plt.xlabel("list2")
plt.ylabel("list3")
plt.title("Question 8 solution")
plt.legend
plt.show()
