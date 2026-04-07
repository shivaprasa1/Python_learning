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


#1) List

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
#1) By remove - specify the value not index
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
ls=[1,2,3,4,5,6,7,8]
print(ls[::2])
print(ls[1::2])
print(ls[:])
print(ls[::-1])
print(ls[len(ls)-1:-1:-1]) # it gives empty becaouse -1 act as last negative index
print(ls[len(ls)-1::-1]) 









#extend vs append vs + 
a=[1,2,3]
b=[5,6,7]
a.extend(b) # iterable each value and store
a.append(b) # it store that obj as value 
c=a+b # create new and combain




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