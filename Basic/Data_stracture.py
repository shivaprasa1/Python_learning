#Data Stracture





#1) List


#creating empty list
"""lst=[]
lst2=list()"""


#
"""lst=[2,5,6,6,9]
for i in range(len(lst)-1 , -1 , -1):
    print(lst[i])"""
    
    
lst=[2,5,6,6,9]

#add
#1) By indexing 
#2) By append



#remove 
#1) By remove - specify the value not index
#2) By pop - not specify it remove last or if specify then it remove that index specify
#3) By del - not specify it remove entire object or list only 
#4) By clear - not specify it remove only values not object

print(lst.remove(6)) # not return the value ----> None
lst.remove(6)
print(lst)

print(lst.pop())   # delete and return the value 