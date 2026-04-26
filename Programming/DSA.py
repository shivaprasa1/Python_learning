
#1) def function decimal to binary 

#using built-in 
"""print(bin(89))
format(89,'b')"""


"""
#
s1=''
for i in range(5):
    s1=s1+str(i) # normal
print(s1)

# 
s2=''
for i in range(5):
    s2=str(i)+s2    # it give last digit to first
print(s2)"""


#without using builtin 

"""def dec_bin(dec):
    bn=""
    while True :
        b = dec%2 
        bn = str(b)+bn      # from last we have cancat
        dec=dec//2
        if dec==0:
            break
    return bn
print(dec_bin(89))"""




#2 - dec to octal 

#built-in 

"""oct(89)
format(89,'o')"""


#without using
"""def dec_oct(dec):
    if dec==0:
        return '0'
    ot=""
    while dec!=0:
        ot=str(dec%8)+ot
        dec//=8
    return ot 

print(dec_oct(89))
   """ 
   



#3 - dec to hex  (hex 0 is  0)

#Built-in
"""hex(89)   # along with 0x it gives
print(format(58,'x'))  #only number format 


#Without built-in

def dec_hex(dec):
    if dec==0:
        return '0'
    hx=""
    while dec!=0:
        r=dec%16
        if r<10:
            hx=str(r)+hx
        elif r==10:
            hx='A'+hx 
        elif r==11:
            hx ='B'+hx 
        elif r==12:
            hx = 'C'+hx 
        elif r==13:
            hx = 'D'+hx 
        elif r==14:
            hx='E'+hx 
        elif r==15:
            hx='F'+hx
        
        dec//=16
    return hx
print(dec_hex(58))
"""






## 65 - 90 (A)
## 97 - 122 (a) ,for zero (0) -  ascii is 48 


#or - using Ascii

"""print(chr(65) , chr(97) , chr(48))

def dec_hex(dec):
    if dec==0:
        return '0'
    hx=''
    while dec!=0:
        r=dec%16
        if dec<10:
            hx=str(r)+hx 
        else:
            hx=chr(r+55)+hx 
        dec//=16 
    """

#or - using string with 0-F
     
"""def dec_hex(dec):
    if dec==0:
        return '0'
    hx=''
    st='0123456789ABCDEF'  
    while dec!=0:
        r=dec%16
        hx=st[r]+hx 
        dec//=16
    return hx 

print(dec_hex(93))"""


# 4) bin to dec 

def bin_dec(bin):
    while bin>0:
        r=bin%10
        dec=0
        for i in range(len(str(bin))):
            dec+=r*2^int(i)
        bin//=10
    return dec  
print(bin_dec(1101))

#or 

"""def bin_dec(bin):
    if bin==0:
        return 0 
    dec=0
    pw=1
    while bin>0:
        r=bin%10
        dec=dec+r*pw
        pw=pw*2 
        bin//=10
    return dec"""



#5)  oct to dec 

"""def oct_dec(bin):
    if bin==0:
        return 0 
    dec=0
    pw=1
    while bin>0:
        r=bin%10
        dec=dec+r*pw
        pw=pw*8 
        bin//=10
    return dec"""
    

#6) hex to dec 
"""
hx='2AB' 
st=""
a=0
for i in hx[::-1]:
    if i==A:
        st=10*16


rev=hx[::-1]"""
 

# ascii to char ----> ord 
# char to ascii ----> chr


"""
int('0',10)#dec
int('2ab',16) #hexa
print(int('101',2)) #binery
print(int('123456',8)) #octal"""
