# This is a simple Python program that demonstrates basic input and output operations.
# It takes user input for two numbers, calculates their sum, and prints the result.


#First program to add two numbers

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
print("Sum of the input number is: ",first+second)

print("...........................")

#Second program to input side of a square and print its area and perimeter
side = float(input("Enter the side of the square: "))
area = side * side
perimeter = 4 * side
print("Area of the square is: ", area)
print("Perimeter of the square is: ", perimeter)

print("...........................")

#Third program to input 2 floating point number and print their average
num1  = float(input("Enter first number: "))
num2 = float(input("Enter second number:"))
average = (num1 + num2)/2
print ("Average of the two number is :", average)

print("...........................")

#Fourth program to input 2 int number,a and b . print True if a is greater than or equal to b, otherwise print False
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
if a>=b:
    print("True")
else:
    print("False")
