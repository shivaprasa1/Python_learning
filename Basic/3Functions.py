#FUNCTION
#Its is block of statements that does specific task

#Advantage
"""
#1)Code reuseabilty - write once use many time
#2)same task deff values
#3)easy to modify
#4)Modularity - code becomes shorter
#5)Readabilty - easy to understand
#6)Maintainabilty"""


#types of functions
"""
1)Builtin 
2)user defined
3)Ananymous (lambda)
"""


# syntax 
#define function using def keyword . A function might take input in the form of parameters.

"""
def function_name ( parameters ):  --------> function declaretion (called functions)
    #statements             ------> body
    return expression 

greet() ---------> calling statements
"""


#arguments or type of arguments
"""
1)posistionel
2)keyword
3)default
4)variable length arg
"""

#example
"""def greet():
    print("hello")

greet()"""


#1) Prime or not in function
def check_prime(num):   #---->positionel arguments
    if num<=1:
        print(num,"not a prime")
        return
    for i in range(2,int(num**2)+1):
        if num%i==0:
            print(num,"not prime")
            return
    print(num,'prime number')

check_prime(39)


#2) def function to check number is a palindrome or not
#3) def function to print max among 3 integers
#4) def functions to check date is valid are not , take three parameters dd-mm-yy
