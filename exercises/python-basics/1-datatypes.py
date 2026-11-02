"""Datatypes and assignment"""

# This file demonstrates the use of different data types in Python.

# TODO: Write correct value types to variables.

a = "Hello, World!"  # String
b = 1                 # Integer
c = 1.0               # Float
d = False             # Boolean

print(a, b, c, d)

print(type(a), type(b), type(c), type(d))

# ----------------------------------------------

"""Lists and dictionaries"""

# TODO: Make a list of 5 numbers and a string and assign it to a variable.
my_list = [1, 2, 3, 4, 5, "six"]  # List

print(len(my_list))

# TODO: Make a dictionary with 3 key-value pairs and assign it to a variable.
my_dict = {"name": "Alex", "age": "25", "city": "Frankfurt"}  # Dictionary

# TODO: Print the keys, values, and items of the dictionary.
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

# TODO: Print the values of specific keys in the dictionary.
print(my_dict["name"])
print(my_dict["age"])
print(my_dict["city"])
