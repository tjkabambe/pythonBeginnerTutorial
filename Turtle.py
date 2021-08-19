# Let's draw some drawings with the package turtle

# Import turtle
import turtle

# Lets get a setup in turtle
# 'bgcolor' is 'background color'
turtle.bgcolor("black")
turtle.pensize(2)
turtle.color("red")
turtle.speed(15)

# # Draw a square
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# # turtle.done() # allows turtle to stay on the screen

# Nice graph in turtle
# for colors in ["red", "blue", "orange", "yellow", "green", "purple"]:
#     turtle.color(colors)
#     turtle.circle(150)
#     turtle.left(60)
# turtle.done()

# to make it better
for i in range(6):
    for colors in ["red", "blue", "orange", "yellow", "green", "purple"]:
        turtle.color(colors)
        turtle.circle(150)
        turtle.left(50)
turtle.done()

