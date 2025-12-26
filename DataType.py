# 1. Numeric Data Types
# Python numbers represent data that has a numeric value. A numeric value can be an integer, a floating number or even a complex number. These values are defined as int, float and complex classes.

a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

# 2. Sequence Data Types
# A sequence is an ordered collection of items, which can be of similar or different data types. Sequences allow storing of multiple values in an organized and efficient fashion. Python has three built-in sequence data types: list, tuple, and range.


# String Data Type
s = 'Welcome to the Geeks World'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1])

# List Data Type
# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed values int and String
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

# Access List Items
a = ["Geeks", "For", "Geeks"]
print("Accessing element from the list")
print(a[0])
print(a[2])

print("Accessing element using negative indexing")
print(a[-1])
print(a[-3])