
#date - 24/3/2026
#________________________________________________________



#Control Statements - contorl the flow of execution

# 1) Conditional Control statements :
                #    A)branching : if, else, elif, nested if -> (it use execute at only one time )
                #    B)looping :for , while  -> (it use when repeatedly executed untill condition becomes False )

# 2) Unconditional Control statements :
#                       break, continue, pass, return










#1) Conditional Control statements :



#if - statements

#Q1) read one value from the user print that integer in positive format

# sourcery skip: avoid-builtin-shadow
"""x=int(input("enter num : "))
if x<0:
    x=x*-1    #convert negative to positive 
    print(x)
else:
    print(x)"""

#or 

"""res="Positive"
if x<0:
    res="Negative"  # reassign or update value
print(res)"""


#Q2 biggest among two decimel number

"""
x=float(input("enter num : "))
y=float(input("enter num : "))
big=x
if y>big:            #reassign 
    big=y
print("biggest among ", x , "and" ,y ,"is" , big)
"""


#hm
"""
Q) 

1)check number is zero or non zero 
-> num=0
print("zero" if num==0 else "non")



2)smallest among two number
-> print(min(a,b))
print(a if a>b else b)



3)check number is even or odd
-> if x%2==0:                    #or x%2 -> it gives either one or zero (1->true and 0->false )
    print(x,"even")
else:
    print(x,"odd")
or
if x%2:
    print(x,"Odd")          # 1 -> True and 0 -> False in bool
else:
    print(x,"even")




4)biggest among three integers
print(x if x>y and x>z else y if y>z else z)




5) check user enter digit is special two digit number or not by using if else
special two digit --------> 59 -> [(5+9)+(5*9)] -> [sum of digit + product of digit] or end with 999999999999

num=59
print((((num//10)+(num%10)) + ((num//10)*(num%10)) ) == num)  

 """




#-----------------------------------------------------

#if - else statements

# zero,none,false,empty set -> falsey
# str,negative or any ->truthy

"""
if "h":               
    print("hello!")
else:
    print("dsffffffff")
    """

"""
x=-10
if x<0:
    print(x,"is negative")
else:
    print(x,"is positive")

"""


#-----------------------------------------------------------------

"""   
#base size 

import sys
sys.getsizeof(10)           # int size start from 28 and varies 
sys.getsizeof(10.5465)      # float size is fixed 24
sys.getsizeof(True)         # act as int i.e 1 ->28
sys.getsizeof(False)        # act as int i.e 0  ->28
sys.getsizeof('A')          #start from 41 and increase len(str)
---------------------------------------------------------------
int       ----> 28 (change)
float     ----> 24 (fixed)
bool(int) ----> 28 (change)
str       ----> 41 (change but depend on str len)

"""












#----------------------------------------------------------------------
#date - 25/03/2026




#if elif and Nested if - statements :



#simple if                                   # if true or false again it will check
"""a=10
b=20
c=30
if a>=b and a>=c:
    print("biggest ",a)
if b>=a and b>=c:
    print("biggest ",a)
if c>=a and c>=b:
    print("biggest ",a)


"""

#if-elif                               # if true , not excute next 

"""if a>=b and a>=c:
    print("biggest ",a)
elif b>=c:
    print("biggest ",b)
else:
    print("biggest ",c)
    
"""




#nested if      
"""
if a>=b:
    if a>=c:
        print('biggest',a)
    else:
        print('biggest',c)
elif b>=c:
    print('biggest',b)
else:
    print('biggest',c)"""





#Q)

#write py prgm to read int value from user if that number is div by 3 -> print Fizz , is number div by 5 -> buzz , if both 3 and 5 -> Fizz and buzz , other wise print number itself


"""user=int(input("enter num "))

if user%3==0 and user%5==0:
    print('Fizz and buzz')
elif user%5==0:
    print('Buzz')
elif user%3==0:
    print('Fizz')
else:
    print(user)


print()

#or



res=('Fizz and buzz' if user%3==0 and user%5==0 else 'Buzz' if user%5==0 else 'Fizz' if user%3==0 else user )

print(res)
"""

#Q) Given a number n, number of apples in a bag. You and your friend are picking one apple turnwise from the bag. It is given that the first attempt is always by you. The person picking the last apple will be the winner.


"""
u=int(input("enter "))
if u%2==0:
    print("You")
else:
    print("Friend")"""


#leap year

# u=int(input("enter "))

"""if u%400==0 or (u%4==0 and u%100!=0):
    print("True")
else:
    print("False")
"""



###########################################################################

#HM 

#1) user read 3 int number , print this 3 num  in ascending order

# user1=int(input("enter num "))
# user2=int(input("enter num "))
# user3=int(input("enter num "))

#approch 01
"""if user1 > user2:
     user1, user2 = user2, user1
if user1 > user3: 
    user1, user3 = user3, user1
if user2 > user3:
     user2, user3 = user3, user2

print(user1, user2, user3)"""



"""
#approch 02 

list=[]
list.append(user1)
list.append(user2)
list.append(user3)
print(sorted(list))
"""


#2) check all 3 distinct or not

# user1=int(input("enter num "))
# user2=int(input("enter num "))
# user3=int(input("enter num "))


#approch 1
"""if user1!=user2 and user1!=user3 and user2!=user3:
    print(user1,user2,user3)
else:
    print("not unique")"""


#approch 2
# A set only keeps unique values
"""if len({user1, user2, user3}) == 3:
    print("All numbers are unique")
else:
    print("not unique")"""


#3) read 3 print only middle sort value

"""
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

if (a<=b and b<=c ) or (c<=b and b<=a):
    middle=b
elif (b <= a and a <= c) or (c <= a and a <= b):
    middle = a
else:
    middle=c
print("The middle value is:", middle)

"""


#4) 4 subj mark students and print pass or fail 

"""a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))
d = int(input("Enter third: "))"""

"""if a<35 or b<35 or c<35 or d<35:
    print("Fail")
else:
    print("Pass")"""



#5) month valid or not

"""month = int(input("Enter first: "))

if month > 0 and month < 13 :
    print("Valid Month")
else:
    print("Invalid Month")
"""

#-------------

#date 26/03/2026

#sir

#1) user read 3 int number , print this 3 num  in ascending order
"""
a = int(input("Enter first: "))
b = int(input("Enter second: "))
c = int(input("Enter third: "))

min=min(a,b,c)         #a if a<b and a<c else b if b<c else c 
max=max(a,b,c)         #a if a>b and a>c else b if b>c else c
mid=(a+b+c)-(min+max)

print(min,mid,max)
"""



#2) mid value finding

"""if a>b and a<c or a>c and a<b:
    print(a)
elif b>a and b<c or b>c and b<a:
    print(b)
else:
    print(c)
"""

#3) subj mark

"""if a>=35 and b>=35 and c>=35 and d>=35:
    print("Pass")
else:
    print("Fail")
"""

# a=200
# b=10
# c=1
# max=(a if a>b and a>c else b if b>c else c)
# min=(a if a<b and a<c else b if b<c else c )
# mid=(a+b+c)-()
# print(min,mid,max) 


#5) month valid or not

"""month = int(input("Enter first: "))

if month < 1 and month > 12 :
    print("InValid Month")
else:
    print("valid Month")
"""



#6 read month num in user and print how many days present in that month number


"""m= int(input("enter month"))

if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    print("31 days")
elif m==4 or m==6 or m==9 or m==11:
    print("30 days")
elif m==2:
    print("28 or 29 days")
else:
    print("invalid")"""


#--------------------------------------------------------------------------------------------------
#problem statements

#1)
"""
Given two numbers a and b. You need to perform basic mathematical operations on them. You will be provided an integer named as operator
If the operator equals to 1 add a and b, then print the result.
If the operator equals to 2 subtract b from a, then print the result.
If the operator equals to 3 multiply a and b, then print the result.
If the operator equals to any other number, print "Invalid Input" (without quotes).
Note: Do not add a new line at the end.
Examples:
Input: a = 1 b = 2 operator = 3
Output: 2
Explanation: 122
Input: a = 2 b = 2 operator = 2
Output: 0
Explanation: 220
"""


"""
a=int(input("enter "))
b=int(input("enter "))
operator = int(input("1.additon \n 2.sub \n 3.multi \n"))

if operator ==1:
    print(a+b)
elif operator ==2:
    print(a-b)
elif operator ==3:
    print(a*b)
else:
    print("Invalid........./")

"""


#2)
# read the date from the user dd-mm-yy formate check date is valid or invalid

"""
dd=int(input())
mm=int(input())
yy=int(input())

if dd<1 or dd>31 or mm<1 or mm>12 or yy<0:
    print('invalid')
elif (mm==4 or mm==6 or mm==9 or mm==11) and dd>30:
    print('invalid')
elif mm==2 and dd>29:
    print('invalid')
elif mm==2 and not(yy%400==0 or yy%4==0 and yy%100!=0) and dd>28:
    print('inavlid')
else:
    print('vaid')"""





#------------------------------

#B)looping


#while - Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. 
#        When the condition becomes false, the line immediately after the loop in the program is executed.



#Q1) 1 to 10 even number 

# n=int(input('enter the value of n'))
"""
x = 2
while x<=n:
    if x%2==0:
        print(x)
    x = x + 1 
    """

#or 
"""x = 2
while x<=n:
    print(x)
    x = x + 2"""

#2) sum of n natural number

# sum=n*(n+1)//2  ----> formula to do sum of n natural number

"""n=5
sum=0    # for add but for mulitiplication --> product = 1
i=1
while i<=n:
    sum=sum+i**3
    i=i+1
print('sum of first ',n,'natural number is ',sum)"""




#3) sum of cube of first naturel number   --> 1^3 +2^3 +3^ .......

#[n*(n+1)//2]**2  ----> sum of cube 

"""n=5
sum=0    
i=1
while i<=n:
    sum=sum+i**3    # cube and add
    i=i+1
print('sum of cube of first ',n,'natural number is ',sum)"""

#or

"""
n=5
sum=(n*(n+1)//2)**2
print(sum)
"""


#4)Count  how many digit in n 

#   // ----> qution (last digit remove)
#   %  ----> remender (give last digit)


# n=int(input("enter the value"))

"""count=0
while n>0:   #true
    n//=10    # don't need this digit=n%10
    count+=1
print(count)"""

#or

# if 0 or single digit 
"""
count=0
while True:     # for single digit we use this 'True' and must ' break' statement is used
    count=count+1
    n=n//10
    if n==0:
        break
print('number of digit ',count)"""



#5) sum of digit in number ----> 2345 == 2+3+4+5 = 9
"""
num=234
sum=0
while num!=0:  # or num>0 
    digit = num%10
    sum+=digit
    num//=10
print(sum)"""




#HM

#1) 1.calculate the factorial of n (5 -> 1^ * 2^ * 3^ * 4^ * 5 = 120 )
"""n=5
fact=1
while n>0:
    fact*=n
    n=n-1
print(fact)
"""

#2) print n to 1

"""
n=5
i=0
while n>0:
    print(n)
    n=n-1
    """


#3)  print the multiple of 5's between 1 to n (i/p:30 o/p:5 10 15 20 25 30)
"""n=int(input('enter num :'))
i=1
while i<=n:
    if i%5==0:
        print(i)
    i+=1
"""

#4) calculate the product of digits (i/p: 234 o/p:24 , ---> 2*3*4)
"""n=int(input("enter a num: "))
product=1
while n>0:
    product*=n%10
    n//=10
print(product)"""


#5) calculate the average of digits (i/p:234 o/p:3)

"""
n=int(input( "enter num"))
count=0
sum=0
while n>0:
    sum+=n%10
    count+=1
    n//=10
print(sum//count)

"""

    


#date - 28/03/2026

#1) reverse number
"""rev=0
x=-1234
while x<=0:
    digit = x%10
    rev=rev*10+digit
    x//=10
print(rev)
"""



#2) Armstrong - sum of power of each length of its digit
"""x=int(input("enter the number :"))
sum,temp=0,x
count=len(str(x))     # count the digit for doing power of it
while x>0:
    digit=x%10
    sum+=digit**count
    x//=10

if sum==temp:
    print(temp,"is Armstrong number")
else:
    print("Not armstrong")
"""

#or

"""start,end=153,10000
while start<=end:
    sum,temp=0,start
    count=len(str(temp))     # count the digit for doing power of it
    while temp>0:
        digit=temp%10
        sum+=digit**count
        temp//=10
    if start==sum:
        print(sum)
    start+=1 """


#3) Dsierium - sum of power of each digit by there position that equal to number    
# 135--> 1^1+3^2+5^3

"""num=int(input("enter the number :"))
sum,temp=0,num

digitcount=len(str(num))

while num!=0:
    digit=num%10
    sum+=digit**digitcount
    digitcount=digitcount-1
    num//=10
if sum==temp:
    print(temp," is a Diserium number")
else:
    print("not Diserium number")"""




#4) Factorial of n - product of number untill it become 1
#range(5) --> range(0,5,1)  
#range(1,5)--->range(1,5,1)
#range(1,5,3)--->range(1,5,3)

# range(start,stop,step)   

"""n=5
fact=1
for i in range(2,n+1):    #n,1,-1
    fact*=i
print("Factorial is",fact)


for i in range(5,0,-1):
    print(i)           # 5 4 3 2 1 


for i in range(5,1,-1):
    print(i)          # 5 4 3 2 
"""


#----------------------------------------------------------

#30/03/2026

#for loop 

# Q1) 20 divisible from 1 to x

"""x=int(input("enter the num"))

for i in range(1,x+1):            #  O(n)
    if x%i==0:
        print(i)


for i in range(1,x//2+1):            #  O(n/2)   ---> any divisible within that half only 
    if x%i==0:
        print(i)"""



# Q2) check the number is perfect number or not (sum its  diviser is equal to that number ) 

"""# num=int(input("enter a num"))
for num in range(100):
    sum=0
    for i in range(1,num//2+1):      # reduce divisable  
        if num%i==0:
            sum+=i
    # print(sum==num)

    if num==sum:
        print(num,'is a perfect number')""" 
    


# Q3) Count how many divises for n
 
#approch - 01
"""n=int(input("enter a num"))
count=1                           # 1 must be inculed
for i in range(1,n//2):
    if n%i==0:
        count+=1
        print(i)
print(count)
"""


#approch - 02
"""n=28
count=list(i  for i in range(1,n//2+1)  if n%i==0  )
print(len(count))
print(count)
"""


#Q4) check user enter integer is prime or not 
"""
n=int(input("enter a num"))
count=1
for i in range(1,n//2+1):
    if n%i==0:
        count+=1
 if count==2:
    print((x,'is prime num'))
else:
    print("not")"""



# Q5)  print all even number within n

"""n=int(input("enter the number"))

for i in range(2,n+1,2):
    print(i,end=" ")"""


#asss
#Q1) print odd between 1 to n and calculate sum of even number and odd number within n
"""n=int(input("enter the number"))"""
"""odd=0
even=0
for i in range(1 , n+1):
    if i%2 :
        print(i)
        odd+=i
    else:
        even+=i

print(odd,even)"""

#q2) print all the odd number from n to 1
"""for i in range(n,1,-1):
    if i%2 :
        print(i)"""


#q3 print multiplication table for user enter number


#Q4)print all the even numbers from n to 1




#-----------------------------------
#date= 31/03/2026 

#assss

#print all the odd number from n to 1
"""x=20
if x%2==0:             # n to 1 only odd 
    x=x-1
for i in range(x,0,-2):
    print(i)
"""


"""if x%2==1:             # n to 1 only even
    x=x-1
for i in range(x,0,-2):
    print(i)"""


# odd sum, even sum
"""n=int(input("enter the number"))"""
"""odd=0
even=0
for i in range(1 , n+1):
    if i%2 :
        print(i)
        odd+=i
    else:
        even+=i

print(odd,even)"""


#print multiplication table for user enter number

"""n=int(input("enter the number"))
for i in range(1,11):
    print(n,'*' , i ,'=' , n*i)"""





#-----------------------------------------------------------------



# 2) Unconditional Control statements :
#                       break, continue, pass, return  , .....exit(function) 


#break - it stop the loop 
"""for i in range(10):
    if i==5:
        break        # stop loop but not entire program
    print(i)
print('thank you')"""  


#continue - it used to stop the current iteration not entire loop
"""for i in range(10):
    if i==5:
        continue        # stop iteration and jump to next iter but not entire loop
    print(i)
print('thank you')"""  


#pass - it acts like a placeholder  or want to use or edit in future than we use this 
"""for i in range(10):
    pass 
"""



#prime

"""count=1
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        count=count+1
    if count>2:
        break
if count==2:
    print("prime")
else:
    print("not primt")

"""

#exit(function) - terminate the program

"""import sys

if n<=1:
    sys.exit()
"""



