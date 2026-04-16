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


#1) List - it is an linear data structure, store multiple values to single variable , also multi datatype , orderd , mutable ,duplicates allowed , flixable size , ..............


#creating empty list
"""lst=[]
lst2=list()"""


#Iterate the list
"""lst=[2,5,6,6,9]
for i in range(len(lst)-1 , -1 , -1):
    print(lst[i])"""
    
    
# lst=[2,5,6,6,9]

#adding element
#1) By indexing  -  assaign a value ----> lst[0]=1
#2) By append    -  it add only ONE element at end --------> lst.append([1,2,3,5]) ---> [1,2,3,5]
#3) By insert    -  insert element at a specific position -----> lst.insert(idx,value) 
#4) By Extend    -  add multiple element ----> lst.extend([1,2,3,5]) ----> 1,2,3,5 



"""
#add
lst[0]=20000
print(lst)
lst.append(10000000)
print(lst)

lst=[1,2,3,4,5]

lst.append([100,400,500,600])
print(lst)

l1=[200,300,700,800,900,1000]
l2=list()
l2.extend(l1)
print(l2)

l2.insert(0,100)
print(l2)
l2.insert(3,400)
print(l2)
"""

#removeing elements
#1) By remove - remove first occurence value not index  ----> lst.remove(value)
#2) By pop -  remove and return ele (default last is remove)---->lst.pop(idx)
#3) By del - not specify it remove entire object or list only 
#4) By clear - it remove all ele not object 


"""ls=[1,2,3,1]

ls.remove(2)
print(ls)
l=ls.copy()
l1=list()

l1.append(ls.pop())
print(l)
print(l1==l)

l1.clear()
print(l1)

del ls[0]
print(ls)"""


#Copy or create duplicate
#1) By Copy
#2) By Sliceing
#3) By loop

"""
ls=[5,4,6,8]
c=ls.copy()
print(c == ls)
print(c is ls)

c1=ls[:]
print(c1)

list=list()
for i in ls:
    list.append(i)
print(list)
 
"""

#Sort
#1)sort - it is method that sort originel obj
#2)sorted - it is function that create separet obj and then sort
#3) reverse - 

"""ls=[1,2,3,4,5]
print(ls.sort(key=None,reverse=True))
print(ls.reverse())
print(ls.copy())
"""


#searching or count
"""#1) index -  search the index and also where to start to find if having same element ---> ls.index(ele,start,end)
ls=[1,2,3,4,5,6,5,6,5,66,66,66,66,88,99,5]
print(ls.index(5,5,8))

#2)count- count occurence
print(ls.count(5))
"""


#Combain two list 
#1) By extend
#2) By cancat or (+)
#3) By append (only one)





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

#Python function 
#1)len()
#2)max()
#3)min()
#4)sum()
#5)sorted()

#type_conversion
#1)list(iterable)
#2)tuple(list)
#3)set(list)

#itration_helpers
#1)enumerate(list)
#2)zip(list1,list2)


list1=[1,2,3,4,5,6]
list2=[7,8,9,10]

v=enumerate(list1)
print(list(v))

for i,x in v:
    print(x) 

print(list(zip(list1,list2)))



#string











#tuple -  it is an linear data structure, store multiple values to single variable , also multi datatype , orderd , immutable ,duplicates allowed , fixed size ,  ..............























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
s1-s2

#symmentic_differnce
s1^s2


"""

a={1,2,3,4}
b={1,2,3,4}
c={4,3,2,1}

print(a==b,a>=b,a<=c)


#checking

#superset  

#subset
#disjoint














