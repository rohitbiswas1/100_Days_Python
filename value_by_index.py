# Write a program in Python to search a value by index.

numbers = [10, 20, 30, 40, 50]
index = int(input("Enter index to search value: "))
if 0 <= index < len(numbers):
    print("The value at index", index, "is:", numbers[index])
else:
    print("Invalid index!")
