# Type Casting a Variable
# Type casting refers to the process of converting the value of one data type into another. Python provides several built-in functions to facilitate casting, including int(), float() and str() among others.

    # Basic Casting Functions
        # int(): Converts compatible values to an integer.
        # float(): Transforms values into floating-point numbers.
        # str(): Converts any data type into a string.

# Example of Type Casting in Python
from ast import Delete


s = "10"  
n = int(s) 
cnt = 5
f = float(cnt)  
age = 25
s2 = str(age)  

print(n)  
print(f)  
print(s2)

# Getting the Type of Variable
# In Python, we can determine the type of a variable using the type() function. This built-in function returns the type of the object passed to it.
n = 42
f = 3.14
s = "Hello, World!"
li = [1, 2, 3]
d = {'key': 'value'}
bool = True

print(type(n))   
print(type(f)) 
print(type(s))   
print(type(li))     
print(type(d))     
print(type(bool))


# Delete a Variable Using del Keyword
# We can remove a variable from the namespace using the del keyword. This deletes the variable and frees up the memory it was using.

x = 10
print(x) 
del x

        # # Trying to print x after deletion will raise an error
        # # print(x)  # Uncommenting this line will raise NameError: name 'x' is not defined
# del x removes the variable x from memory.
# After deletion, trying to access the variable x results in a NameError indicating that the variable no longer exists.

# 1. Swapping Two Variables
# Using multiple assignments, we can swap the values of two variables without needing a temporary variable.
a, b = 5, 10
a, b = b, a
print(a, b)

# 2. Counting Characters in a String
# Assign the results of multiple operations on a string to variables in one line.


word = "Python"
length = len(word)
print("Length of the word:", length) 