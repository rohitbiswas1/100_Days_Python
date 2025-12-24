# 1. Numeric Data Types
# Python numbers represent data that has a numeric value. A numeric value can be an integer, a floating number or even a complex number. These values are defined as int, float and complex classes.


a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

# 2. Sequence Data Types
# of multiple values in an organized and efficient fashion. There are several sequence data types of Python:

s = 'Welcome to the Geeks World'
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1])

l = [1, 2, 3, 4, 5]

# List Data Type
# Lists are similar to arrays found in other languages. They are an ordered and mutable collection of items. It is very flexible as items in a list do not need to be of the same type.

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

# Tuple Data Type

# Tuples can also be created with a single element, but it is a bit tricky. Having one element in the parentheses is not sufficient, there must be a trailing ‘comma’ to make it a tuple. 

# initiate empty tuple

tup1 = ()

tup2 = ('Geeks', 'For')
print("\nTuple with the use of String: ", tup2)

# Access Tuple Items
tup1 = (1, 2, 3, 4, 5)

# access tuple items
print(tup1[0])
print(tup1[-1])
print(tup1[-3])

# 3. Boolean Data Type
# Python Boolean Data type is one of the two built-in values, True or False. Boolean objects that are equal to True are truthy (true) and those equal to False are falsy (false). However non-Boolean objects can be evaluated in a Boolean context as well and determined to be true or false. It is denoted by class bool.


print(type(True))
print(type(False))
print(type(true))

# Truthy and Falsy Values
# In Python, truthy and falsy values are values that evaluate to True or False in a Boolean context. Truthy values behave like True, while falsy values behave like False when used in conditions.

if 1:
    print("1 is truthy")

if not 0:
    print("0 is falsy")

# 4. Set Data Type
# In Python Data Types, Set is an unordered collection of data types that is iterable, mutable, and has no duplicate elements. The order of elements in a set is undefined though it may consist of various elements.

# Create a Set in Python
# initializing empty set
s1 = set()

s1 = set("GeeksForGeeks")
print("Set with the use of String: ", s1)

s2 = set(["Geeks", "For", "Geeks"])
print("Set with the use of List: ", s2)

# Access Set Items

set1 = set(["Geeks", "For", "Geeks"]) #Duplicates are removed automatically
print(set1) 

# loop through set
for i in set1:
   print(i, end=" ") #prints elements one by one
  
# check if item exist in set   
print("Geeks" in set1)

# 5. Dictionary Data Type
# A dictionary in Python is a collection of data values, used to store data values like a map, unlike other Python Data Types, a Dictionary holds a key: value pair. Key-value is provided in dictionary to make it more optimized. Each key-value pair in a Dictionary is separated by a colon : , whereas each key is separated by a ‘comma’.
# Create a Dictionary in Python
# initialize empty dictionary
d = {}

d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

# Accessing Key-value in Dictionary
d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))









