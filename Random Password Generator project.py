# Mini project - Random Password Generator project

# Importing relevant modules
import random

# All uppercase password
password = ""
for i in range(10):
    i = chr(random.randint(65, 90))
    password = str(password) + i
print(password)

# Upper and Lowercase password
password = ""
for i in range(5):
    i = chr(random.randint(65,90))
    for  j in range(5):
        j = chr(random.randint(65, 90)).lower()
    password = str(password) + i + j
print(password)

