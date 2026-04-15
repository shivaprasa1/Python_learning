#Data Stracture - Allocating or arrange the elements in memory 
#two way to store or allocating the elements
#1) Continous
#2) node or linkedlist

#two type of Data structure
#1) Built-in
#2) User defined 

#1) Built-in Data Structure
#(i) List
#(ii)Tuple
#(iii)set
#(iv)dict


#1) List - it is an linear data structure, store multiple values to single variable , also multi datatype , orderd , mutable ,duplicates allowed..............


#creating empty list
"""lst=[]
lst2=list()"""


#Iterate the list
"""lst=[2,5,6,6,9]
for i in range(len(lst)-1 , -1 , -1):
    print(lst[i])"""
    
    
# lst=[2,5,6,6,9]

#add
#1) By indexing 
#2) By append
#3) By insert


#remove 
#1) By remove - specify th e value not index
#2) By pop - not specify it remove last or if specify then it remove that index specify
#3) By del - not specify it remove entire object or list only 
#4) By clear - not specify it remove only values not object

#Copy or create duplicate
#1) By Copy
#2) By Sliceing
#3) By loop

#Sort
#1)sort - it is method that sort originel obj
#2)sorted - it is function that create separet obj and then sort


#reverse 
"""ls.reverse()"""


#Combain two list 
#1) By extend
#2) By cancat or (+)
#3) By append (only one)


#Python function 
#1)len()
#2)max()
#3)min()
#4)sum()
#5)sorted()


#Slicing on list
"""ls=[1,2,3,4,5,6,7,8]
print(ls[::2])
print(ls[1::2])
print(ls[:])
print(ls[::-1])
print(ls[len(ls)-1:-1:-1]) # it gives empty becaouse -1 act as last negative index
print(ls[len(ls)-1::-1]) """




#extend vs append vs + 
"""a=[1,2,3]
b=[5,6,7]
a.extend(b) # iterable each value and store
a.append(b)""" # it store that obj as value 
# c=a+b # create new and combain




"""
#add
lst[0]=20000
print(lst)
lst.append(10000000)
print(lst)


#delete or remove
print(lst.remove(6)) # not return the value ----> None
lst.remove(6)
print(lst)
print(lst.pop())   # delete and return the value
print(lst)
del lst[0]
print(lst)
#del lst # delete obj
lst.clear() # delete values
print(lst)"""



#Nested List

"""ls=[1,2,[5,6,9],6]
print(ls[2][0])
"""
# ls2=[[1,2,3],[4,5,6],[7,8,9]]
# for i in ls2:
#     for j in i:
#         print(j)

"""
for i in ls:
    if isinstance(i,list):
        for j in i:
            print(j)
    else:
        print(j)

"""
        

# print(chr(65),chr(97))






#string











#tuple





#DICT




#SET 

"""
#set not allow duplicate
#set is not orderd
#set inside set not allow mutable datatype but only allow immutable
#set is mutable
#not index based
#set not support slicing

"""


"""
s1={} #----> dict
s1={1,"shiva",3.1} #---->SET

s2={{1:"shiva"},[1,2,3]} #----> not allowed mutable datatype inside set
print(s2)
"""

#adding to set

#add 
#update

"""ages=set()
type(ages)

ages.add(34)
ages.add(56)
ages.add(29)
ages.add(56) #duplicate not allowed
print(ages)


#remove duplicate from list
ls=[3,4,5,3,4,7,4,6,5]

#itrate 
uls=set()
for ele in ls:
    uls.add(ele)
print(uls) 

#Type caste
uele=set(ls)
print(uele)


"""


#add vs update

"""t1=(1,2,3,5)
s1={5,6,9,2}

ls=[100,222,666]
s1.add(t1) # obj is store
s1.update(t1) #each ele is store
s1.update(ls)  # list cannot add but we can update
print(s1)"""


#delete

#remove - specify ele
#pop - random ele
#dicard - specify and give error
#clear  - remove all ele
#del - remove obj



#remove vs discard

"""s1.remove(1)
s1.remove(100000)#gives error

s1.discard(2)
s1.discard(1000000000)#not give any error

"""
"""#pop
s1={5,6,9,2}

print(s1.pop()) # randomly remove from the set and return ele
print(s1)

#clear vs del

s1.clear()
del s1


#copy vs alias

s1={5,6,9,2}
s2=s1 #it change
s3=s1.copy() # it create duplicate

#addition and multipliction not allowed

s1+s2 
s1*s2


#union

s1.Union(s2) #combines and return new set
u=s1|s2 # same but not return


#intersection

s1.intersection(s2)
s1&s2

#difference


"""















