#FUNCTION
#Its is block of statements that does specific task

#Advantage
"""
#1)Code reusability - write once use many time
#2)same task different values
#3)easy to modify
#4)Modularity - code becomes shorter
#5)Readability - easy to understand
#6)Maintainability

 """


#types of functions
"""
1)Builtin 
2)user defined
3)Anonymous (lambda)
"""


# syntax 
#define function using def keyword . A function might take input in the form of parameters.

"""
def function_name ( parameters ):  --------> function declaration (called functions)
    #statements             ------> body
    return expression 

greet() ---------> calling statements
"""


#arguments or type of arguments
"""
1)positional
2)keyword
3)default
4)variable length arg
"""

#example
"""def greet():
    print("hello")

greet()"""


#1) Prime or not in function
"""def check_prime(num):   #---->positional arguments
    if num<=1:
        print(num,"not a prime")
        return
    for i in range(2,int(num**2)+1):
        if num%i==0:
            print(num,"not prime")
            return
    print(num,'prime number')

check_prime(39)"""


#2) def function to check number is a palindrome or not

#approach 1:
"""def palindrome(num):
    rev=""
    for i in str(num):
        rev+=i
    r=rev[::-1]
    print(int(r)==num)

palindrome(121)"""

#approach 2:
"""def palindrome(num):
    org=num
    rev=0
    while num>0:
        rev=rev*10+num%10
        num//=10
    print(rev==org)
palindrome(121)"""


        
#3) def function to print max among 3 integers
#approach 1:
"""def max1(a,b,c):
    if a>b:
        if a>c:
            print(a)
        else:
            print(c)
    elif b>c:
        print(b)
    else:
        print(c)

max1(5000,5465,68549)"""


#approach 2:
"""def max2(a,b,c):
    return a if a>b and a>c  else b if b>c else c

print(max2(50,100,300))
"""


#4) def functions to check date is valid are not , take three parameters dd-mm-yy
"""def check_date(dd,mm,yy):
    if dd<=0 and dd>31 and mm<=0 and mm>12 and y<0:
        print("Invalid date")
    elif (mm==4 or mm==6 or mm==9 or mm==11) and dd>30:      # 4,6,9,11 -----> don't have 31 in month
        print('invalid')
    elif mm==2 and dd>29:         
        print('invalid')
    elif mm==2 and not(yy%400==0 or yy%4==0 and yy%100!=0) and dd>28:
        print('invalid')
    else:
        print('valid') 
check_date(19,2,2023)"""


#5) check 3 integer are equal or not
"""def equal(a,b,c):
    if a==b==c :
        print("equal")
    else:
        print("not equal")

equal(5,6,6)"""

#6) def function take 4 subj marks of students print is pass or fail , if pass print his grade 
"""def marks(s1,s2,s3,s4):
    if s1<0 and s1 > 100 or (s1<0 and s1 > 100) or ( s1<0 and s1 > 100) or ( s1<0 and s1 > 100):
        print("invalid marks")
    if s1 > 35 and s2>35 and s3>35 and s4>35:
        print("All subject pass")
        Percentage = (s1+s2+s3+s4)*100 /100  
        if percentage > 80:
            print('grade A ")
        elif percentage < 80 and percentage > 50:
            print("grade B")      
    else:
        print("fail")

marks(50,100,80,60)
"""
#or

def printresult(p,c,m,b):
    if p<35 or c<35 or m<35 or b<35:
        print("Fail")
    else:
        per=(p+c+m+b)/4
        if per>=85:
            print("distinction")
        elif per>=60:
            print("First class")
        elif per>=50:
            print("second")
        else:
            print("just pass")
            
            
            
            
        
        
# def function to written first digit of number

"""def digit(num):
    if num <0:
        num=num*-1
    while num>=10 or num<-9:
        num//=10
    return num 
print(digit(-95))

"""

#or
"""import math
def digit(x):
    if x<0:                                                    #  two - 10 , three - 100  
        x=x*-1
    ct = int(math.log10(x))
    return x//10**ct
print(digit(123))
"""



# def function to return how many prime digit present in the number


"""def prime_count(num):
    count=0
    while num>0:
        digit=num%10
        for i in range(2,int(digit**0.5)+1):
            if num%i!=0:
                count+=1
        num//=10
    return count

print(prime_count(2357))"""

#or 

def count_prime(n):
    count=0
    while n!=0:
        d=n%10
        if d==2 or d==3 or d==5 or d==7:     # if d in [2,3,5,7]
            count+=1
        n=n//10
        return count





#Deault arg
#assaning a value to any arguments or para at the time of declartion or fn def
# default must write after all the positinol
""""def fun(a=0):
    print('value is ',a)
fun(10)
fun()
fun("abc")


def sum(a=0,b=0):
    print('a value is : ' ,a)
    print('b value is : ' ,b)
    print('value is : ' ,a+b)

def prod(a=1,b=1):
    print('a value is : ' ,a)
    print('b value is : ' ,b)
    print('value is : ' ,a*b) 
    


def bill(price,tax=0.18):
    print('price is ',price)
    ttax=price*tax
    print('tax applied',ttax)
    total=price+ttax  
    print('total bill',total)""""
    
    
    
# def function num is a desierm num 
#def function to return avg of digit
#def function to return true if the num is the strong number otherwise return false
#def function to return reverse of the num
#def function to return true if the num is happy number otherwise return false

