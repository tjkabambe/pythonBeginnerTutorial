# Import relevant modules
import matplotlib.pyplot as plt

# Plotting Graphs in Python
# Basic plot
# x = [2, 4, 7, 11, 16, 22]
# plt.plot(x)
# plt.show() # Shows the plot we are plotting

# Plotting x and y against each other
# y = [1, 3, 6, 10, 15, 21]
# plt.plot(x, y)
# plt.show()

# Something nice
# Line 1 - Points

x = [3, 9, 20]
y = [2, 7, 50]

# Plotting x and y
plt.plot(x, y, c="red", linewidth=2, label = "Line 1")

# Line 2 - points
x2 = [1, 15, 30]
y2 = [4, 11, 40]

# Plotting x2 and y2
plt.plot(x2, y2, c="blue", linewidth=2, label = "Line 2", linestyle="dashed",
         marker = "o", markerfacecolor="orange", markersize=10)

# Label the axes
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.title("Two Lines!")

# Limits of the axes
plt.ylim(1,10)
plt.xlim(0,30)

# Show legend on plot
plt.legend()

# Python to show the entire graph
plt.show()