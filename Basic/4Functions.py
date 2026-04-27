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
4)variable length arg - i) variable length positional arg 
                        ii) variable length keyword arg
"""

#example
"""def greet():
    print("hello")

greet()"""



#positional

#1) Prime or not in function
"""def check_prime(num):   #---->positional arguments
    if num<=1:
        print(num,"not a prime")
        return
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print(num,"not prime")
            return
    print(num,'prime number')

check_prime(3)"""


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

"""def printresult(p,c,m,b):
    if p<35 or c<35 or m<35 or b<35:
        print("Fail")
    else:
        per=(p+c+m+b)/4             #------------> avg or percentage same
        if per>=85:
            print("distinction")
        elif per>=60:
            print("First class")
        elif per>=50:
            print("second")
        else:
            print("just pass")"""
            
            

        
# def function to written first digit of number

"""
def digit(num):
    y=num
    if num <0:
        num=num*-1
    while num>=10 or num<-9:       #  -10 < -9 < -8 < -7 < -6  < -5 < -4 < -3 < -2 < -1 <<<<< 0 <<<<<< 1 < 2 < 3 < 
        num//=10
    return num*-1 if y < 0 else num 
print(digit(-156))

"""
# print(max(-8,-9))   # max is -8 


#or

"""
import math
def digit(x):
    if x<0:                       #  two - 10 , three - 100  , fourth - 1000  --->10 power of this  (if we do log10 to any number it give n-1 digit) 
        x=x*-1
    ct = int(math.log10(x))
    return x//10**ct
print(digit(5))
"""




# def function to return how many prime digit present in the number


"""
def prime_count(num):
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
"""
def count_prime(n):
    count=0
    while n!=0:
        d=n%10
        if d==2 or d==3 or d==5 or d==7:     # if d in [2,3,5,7]
            count+=1
        n=n//10
        return count
"""


#-------------------------------------------------------------------------------------------------

#Default arg
#assaning a value to any arguments or para at the time of declartion or fn def
# default must write after all the positinol
"""def fun(a=0):
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
    print('total bill',total)"""
    
    
    
# def function num is a desierm num 
"""def desierm(num):
    temp=num
    digit=0
    count=len(str(num))
    while num>0:
        digit+=(num%10)**count
        count=count-1
        num//=10
    return digit==temp 
print(desierm(135))
"""

#def function to return avg of digit
"""def avg(num):
    summ=0
    count=len(str(num))
    while num >0:
        summ+=(num%10)/count
        num//=10
    return summ

print(avg(1234))"""
        
#def function to return true if the num is the strong number otherwise return false
"""def strong(num):
    temp=num
    digit=0
    strong=0
    while num >0:
        digit=num%10
        fact=1
        for i in range(1,digit+1): 
            fact*=i
        strong+=fact
        num//=10
    return strong==temp

print(strong(145))"""
            
        
#def function to return reverse of the num
"""def rev(num):
    rev=0
    while num>0:
        rev=rev*10+(num%10)
        num//=10
    return rev
print(rev(123456))
"""

#def function to return true if the num is happy number otherwise return false ----> sum of square of each digit until it become one or 7
"""
num=12
def happy(num):  
    while num>9:  
        digit=0
        for i in str(num):
            digit+=int(i)**2
        num=digit
    return num==1 or num==7

print(happy(19))"""



#------------------------------------------------------------------------------------------------------


#keywaord arguments
# spcifying the parameter name in calling statements         
# Order is not require
# always first is positionel arguments then keywords or default at last


#Example
"""
def area_rect(length,breadth):
    print('Area is ', length*breadth)
    print('perimeter is ', 2*(length + breadth))
area_rect(breadth=8,length=10)   #--------------> keyword arguments

"""


# Q1) def function to write GCD of any two number


#approch - 01
"""def gcd(n1,n2):
    gcd=1 
    i=1
    while i<=n1 and i<=n2:
        if n1%i==0 and n2%i==0:
            gcd=i
        i+=1
    return gcd
print(gcd(12,18))"""
    
#approch - 02

"""def gcd(m,n):
    while(m!=0):
        t=m 
        m=n%m       #m,n=n%m,m
        n=t 
    return n
print(gcd(8,16))"""

# 
"""def info(name,age):
    print(name,age)
info(name="prasad","hb") #error first always positional
"""


#Both default , positionel , keyword
"""
def profile(age=None,name=None,mob=None):
    print("name",name)
    print("age:",age)
    print("mob:",mob)
profile()
profile(25,name="shivu",mob=12346789)
"""


"""
def var(**arg):
    print(arg)
    
    
var(name="shiva",mob=123456789,place="Mysore")

"""


# 4)variable length arg - i) variable length positional arg 
#                         ii) variable length keyword arg
#i) variable length positional arg
"""def fun(*t):
    print(t)
print(fun(1,2,3,5,5,1,5,585))
"""

#ii) variable length keyword arg

"""def fun(**kw):
    for k,w in kw.items():
        print(k,w)

print(fun(radius=10,length=100,breadth=500))"""


"""
def print_it(i,j,*arg,x,y,**kw):
    print(i,j)
    print(arg)
    print(x,y)
    print(kw)

print(print_it(1,2,5,6,4,8,9,6,2,x=100,y=200,a=500,b=600))  # after positional we cant write anything if want then we must write keyword arg

#order - (positional , variable length argu,keyword argu , variable length keyword argu)"""


"""#unpack lst , tuple,set
def fun(a,b,c):
    print(a,b,c)
ls=[1,2,3]
print(fun(*ls))"""
"""
def disp(name='shivu',marks=100):
    print('name :',name)
    print('marks :',marks)

dict={'namee':'shivoooo','marks':200}
print(disp(*dict)) # only take key from dict if we used positional variable legnth argu
print(disp(**dict)) # error if give dict key name is diffrent from parameter """




#23/04/26
#----------------------------------------------

#recursion: function calling itself 
#a) base condition to stop call itself
#b) calling statement to call itself


#
"""def m1():
    print('i am m1')
    m2()
                                # cycling calling
def m2():
    print('iam m2')
    m1()
    

#---

def demo():
    print('i am demo')
    demo()   # calling statement to call itself  and must have base condtion if not it will go infinite time
    """
    
    
    
#1) head recursion  - recursion in fast
"""def headprint(n):
    if n==0:
        return
    headprint(n-1)   #after calling all it again print from back 
    print(n)

headprint(5)"""


#2) tail recursion - recursion in last
"""
def tailprint(n):
    print(n)
    if n>1:
        tailprint(n-1)
tailprint(3) """


#default limit in recursion - 10^4 or 10^3

#we can set limit function ---> sys module

#----------------------------------

#example 

# 1) factorial 
#5!=5*4*3*2*1
#1!=1
#0!=1

# 5!=5*4!
# n!=n*(n-1)!

"""def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)

print(fact(5))"""

# 2) sum of n naturel
"""def sumofn(n):
    if n==0:
        return 0
    return n+sumofn(n-1)
print(sumofn(5))"""


#3) sum of digit
"""def sumofd(n):
    if n==0:
        return 0
    return n%10+sumofd(n//10)
print(sumofd(12345))"""



#4) count digit in number
"""def countd(n):
    if n>=-9 and n<=9:
        return 1
    return 1+countd(n//10)

print(countd(-568))

print(-569 > -9)"""

#5) decemil to bin

"""def dec_bin(n):
    if n==0:
        return '0'
    return dec_bin(n//2)+str(n%2)
print(dec_bin(4))"""

#6) search specified element present the number or not

"""ls=[]
def search(ls,ele,idx=0):
    if idx==len(ls):
        return None
    if ls[idx]==ele:
        return idx
    return search(ls,ele,idx+1)

print(search(ls,9))"""

#sum of num in list

"""def sum(ls,idx=0):
    if idx==len(ls):
        return 0
    return ls[idx]+sum(ls,idx+1)"""


