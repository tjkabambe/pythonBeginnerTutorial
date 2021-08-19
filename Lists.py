my_list1 = [1, 2, 3, 4, 5, 6]
my_list2 = list(range(2, 50, 2*3))
print(my_list1)
print(my_list2)
print(my_list2[-1])
print(my_list1[0:4])
# length of list
print(len(my_list2))
# Maximum number and Minimum number of a list
print(max(my_list2))
print(min(my_list2))

# Add an element to a list
my_list1.append(7)

print(my_list1)

# Reverse a list
my_list1.reverse()
print(my_list1)

# Create another list and add two lists together
my_list3 = [10, 20, 30, 40, 50, 60]

print (my_list1 + my_list3)