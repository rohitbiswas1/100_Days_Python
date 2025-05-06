# Basics of Strings
str0 = "\nHello coders"
str1 = '\nHello coders'
str2 = '''\nHello coders'''
str3 = "\nHello coders.\nhow are you?"  # \n is used to create a new line
str4 = "\nHello guys. \tAre you ready to learn Python?"  # \t is used to create a tab space

# Print the strings
print(str0)
print(str1)
print(str2)
print(str3)
print(str4)

# String Concatenation
str5 = str3 + str4  # Concatenation of two strings
print(str5)

# Length of Strings
print("Length of str3:", len(str3))
print("Length of str5:", len(str5))

# Indexing of Strings
# Indexing is used to access characters in the string
print("Character at index 7 of str4:", str4[7])
chr0 = str5[0]  # Accessing the 0th index of str5
print("First character of str5:", chr0)

# Slicing of Strings
# Slicing is used to access a portion of the string
name = "Rohit Sharma"
print("Slice from index 0 to 6:", name[0:7])  # Includes index 0 to 6
print("Slice from beginning to index 3:", name[:4])  # Includes index 0 to 3
print("Slice with negative index [-1:-4]:", name[-1:-4])  # This will return an empty string


#Sting Functions 

#str.endwith() function is used to check itf the string ends with the specified value.
#It returns True if the string ends with the specified value, otherwise it returns False.
#Example:
print(name.endswith("ma"))
print(name.endswith("Img"))

#str.captalize() function is used to convert the first character of the string to uppercase and the rest to lowercaser.
#It returns the modified string.
#Example:

cap = "my name is Rohit"
print(cap.capitalize())
cap = cap.capitalize()
print(cap)


#str.replace() function is used to replace a specified value with another value in the string:
#Example:


