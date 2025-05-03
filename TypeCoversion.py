#Type Conversion
#Type conversion is the process of converting a value from one data type to another.

# Implicit Type Conversion (Python automatically converts)
a = 5       # int
b = 2.0     # float

result = a + b  # int + float => float
print("Result:", result)
print("Type of result:", type(result))  # Output: <class 'float'>


# Explicit Type Conversion (you convert manually)
x = "10"
y = "3.5"

# Convert strings to int and float
x_int = int(x)
y_float = float(y)

sum_result = x_int + y_float
print("Sum after conversion:", sum_result)
print("Type of sum_result:", type(sum_result))  # Output: <class 'float'>

#Type custing 

a = "15"     # string
b = 4        # int

# Convert 'a' to int before adding
result = int(a) + b
print("Result:", result)         # Output: 19
print("Type:", type(result))     # <class 'int'>

