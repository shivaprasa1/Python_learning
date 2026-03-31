# Operators - it is symbols which are operates with operands  or it perform operation on operands
#Operands --> values or variable 

"""Types of operators
1) Unary ---> bitwise + , bitwise  - , logical not , bitwise not (~) 
2) Binary ---> Arthmatic , logical , membership , identity , assignment , bitwise 
3) Ternary ----> if , else """


#1) Unary -  a unary operator acts on a single operand to produce a new result.

num = 5
result = +num # result is 5

num = 5
result = -num # result is -5

is_active = True
result = not is_active # result is False


num = 5      # Binary: ...00000101
result = ~num # Binary: ...11111010 (which is -6 in two's complement)


"""
Unpacking Operators (* and **): 
In specific contexts, the single asterisk (*) and double asterisk (**) are used as unary operators for unpacking elements 
from iterables (like lists or tuples) and dictionaries, respectively, often when passing arguments to functions. 
"""

def my_func(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]
my_func(*my_list) # Unpacks the list into arguments

#-----------------------------------------------------------------------------------------------------------------------------------------

# 2) Binary - a binary operator is one that operates on two operands

# i) Arithmetic Operators  - Arithmetic operators are used to perform basic mathematical operations like addition, subtraction, multiplication and division.

# Variables
a = 15
b = 4
# Addition
print("Addition:", a + b)  

# Subtraction
print("Subtraction:", a - b) 

# Multiplication
print("Multiplication:", a * b)  

# Division
print("Division:", a / b) 

# Floor Division
print("Floor Division:", a // b)  

# Modulus
print("Modulus:", a % b) 

# Exponentiation
print("Exponentiation:", a ** b)



#ii) Comparison Operators - Comparison (or Relational) operators compares values. It either returns True or False according to the condition.
  
a = 13
b = 33​
print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)


#iii) Logical Operators - Logical operators perform Logical AND, Logical OR and Logical NOT operations. It is used to combine conditional statements.

"""
The precedence of Logical Operators in Python is as follows:
Logical not
logical and
logical or 
"""

a = True
b = False
print(a and b)
print(a or b)
print(not a)

#iv) Bitwise Operators -Bitwise operators act on bits and perform bit-by-bit operations. These are used to operate on binary numbers.

"""
Bitwise Operators in Python are as follows:
Bitwise NOT
Bitwise Shift
Bitwise AND
Bitwise XOR
Bitwise OR
"""
a = 10
b = 4​
print(a & b)
print(a | b)
print(~a)
print(a ^ b)
print(a >> 2)
print(a << 2)


#v) Assignment Operators - Assignment operators are used to assign values to the variables. 
# This operator is used to assign the value of the right side of the expression to the left side operand. Example:

a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)

Output
10
20
10
100
102400



#vi) Identity Operators - "is" and "is not" are the identity operators and 
#both are used to check if two values are located on the same part of the memory.

"""
Two variables that are equal do not imply that they are identical. 

is          True if the operands are identical 
is not      True if the operands are not identical 
"""

a = 10
b = 20
c = a
​
print(a is not b)
print(a is c)

Output
True
True



#vii) Membership Operators - "in" and "not in" are the membership operators that are used to test whether a value or variable is in a sequence.

""" 
in            True if value is found in the sequence
not in        True if value is not found in the sequence
"""



x = 24
y = 20
list = [10, 20, 30, 40, 50]
​
if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")
​
if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

"""
Output
x is NOT present in given list
y is present in given list
"""



#---------------------------------------------------------------------------------------------------------------------------------------------

#3) Ternary Operator - Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false.
# It was added to Python in version 2.5. 

"""
It simply allows testing a condition in a single line replacing the multiline if-else, making the code compact.
Syntax :  [on_true] if [expression] else [on_false] 
"""
#1 min of two num
a, b = 10, 20
min = a if a < b else b
print(min)

#2 special two digit (sum + product = given number or ends with 9 )
x=59
d1=x//10
d2=x%10
sum=d1+d2+d1*d2
res="special" if sum == x else "not special"
print(res)





