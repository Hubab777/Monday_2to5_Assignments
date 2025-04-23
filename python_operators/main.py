# Class Assignment : 2
# Day: Monday 2-5 pm
# Topic: Python Operators

# 1. Arithmetic Operators
# Used to perform basic mathematical operations.

a = 10
b = 3
print("\n-----------'ARITHMETIC OPERATORS'-----------\n")

# Addition - Adds two numbers
print(a + b)   

# Subtraction - Subtracts second number from first
print(a - b)   

# Multiplication - Multiplies two numbers
print(a * b)  

# Division - Divides first number by second (returns float)
print(a / b)   

# Modulus - Returns remainder of division
print(a % b)   

# Exponentiation - Raises first number to the power of second
print(a ** b) 

# Floor Division - Returns quotient without decimal part
print(a // b)  


# 2. Assignment Operators
# Used to assign and update variable values.

x = 5
print("\n-----------'ASSIGNMENT OPERATORS'-----------\n")

# Add and assign
x += 3      

# Subtract and assign
x -= 2      

# Multiply and assign
x *= 4      

# Divide and assign
x /= 2      

# Modulus and assign
x %= 3      

# Exponentiate and assign
x **= 2    

# Floor divide and assign
x //= 2     

# Final result of x
print(x)   


# 3. Comparison Operators
# Used to compare two values, returns True or False.

a = 5
b = 7

print("\n-----------'COMPARISON OPERATORS'-----------\n")

# Equal to
print(a == b)   

# Not equal to
print(a != b)   

# Greater than
print(a > b)   

# Less than
print(a < b)    

# Greater than or equal to
print(a >= b)   

# Less than or equal to
print(a <= b)   


# 4. Logical Operators
# Used to combine multiple conditions (boolean values).

a = True
b = False

print("\n-----------'LOGICAL OPERATORS'-----------\n")

# AND - True if both are True
print(a and b)  

# OR - True if at least one is True
print(a or b)   

# NOT - Reverses the result
print(not a)   


# 5. Identity Operators
# Used to compare memory locations of two objects.

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("\n-----------'IDENTITY OPERATORS'-----------\n")

# is - True if both refer to same object
print(a is b)      

# is not - True if both refer to different objects
print(a is not c)  


# 6. Membership Operators
# Used to test if a value is in a sequence.

print("\n-----------'MEMBERSHIP OPERATORS'-----------\n")

fruits = ['apple', 'banana', 'cherry']

# in - True if value exists in the sequence
print('banana' in fruits)     

# not in - True if value does not exist in the sequence
print('grape' not in fruits)  


# 7. Bitwise Operators
# Used to perform bit-level operations.

a = 5  # Binary: 0101
b = 3  # Binary: 0011

print("\n-----------'BITWISE OPERATORS'-----------\n")

# AND - Sets each bit to 1 if both bits are 1
print(a & b)   

# OR - Sets each bit to 1 if one of the bits is 1
print(a | b)   

# XOR - Sets each bit to 1 if bits are different
print(a ^ b)   

# NOT - Inverts all bits
print(~a)      

# Left shift - Shifts bits to the left
print(a << 1)  

# Right shift - Shifts bits to the right
print(a >> 1)  