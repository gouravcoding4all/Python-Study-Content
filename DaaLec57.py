"""
Sequence Data type
    List,tuple(based on index)
Hash Data Type
    set,Dictionary

Set:-Set is an unordered(order is not preserved) collection of unique(no duplicate) hetrogenous(different data types) elements

s={12,34,4,56,78}
s={23,56,34,3+8j,'Aman',True}
s=set()
s=set([2,45,68])
s=set((2,45,68))
s=set({2,45,68})
print(s)
print(type(s))

It will remove the dulplicate values and order will not preserved.
python computes its hash values using hash()
The hash determines where the element is stored
if another element hashes to the same location (a collision),python resolves it internally
since each hash key represents one unique value, duplicates are not stored

-set stores unique elements only
-unordered collection
-backed by has table ,making lookups,insertions,deletion very fast
-Elements must be hashable(int,strings,float,tuples)
-Mutable type like lists (can not added to a set)

s={23,(23,455,67,76),[23,45,67,87],45,67,8}
print(s)
#A Set can not store List

#set has no Index
#Set can not be sliced
#Set can not be Replicate
#but,set can be TRAVERSE/ITTERATE

s={12,78,25,12,85,35,62}
print(s)
for a in s:
    print(a)

#Built-in functions
    sum,max,min,len

s={12,78,25,12,85,35,62}
print(s)
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

SET's Methods
add,pop,remove,discard,update
s={10,20,30,40}
print(s)
s.add(50)   #add on a random location
print(s)

li=[60,70,30,80]
s.update(li)    #to add multiple elemrnts on a random location
print(s)
s.pop()     #pop will remove a random element
print(s)

s={10,20,30,40,50,60,101}
s.remove(50)        # remove element '50'
print(s)
# s.remove(101)           # raise an error, 101 is not available
s.discard(60)       # remove element '60'
print(s)
s.discard(101)            # will not raise any error
print(s)
SET's Method
union ,intersection,difference,symmetric_difference

s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
print(s1.union(s2)) #add both sets but will not repeat elements
print(s1.intersection(s2))  #print only common elements
print(s1.difference(s2))    #remove common elements from s1 and print   s1
print(s1.symmetric_difference(s2))  #add both sets n remove common elements


"""

s1={1,2,3,4,5,6}
s2={4,5,6,7,8,9}
print(s1 & s2) #intersection
print(s1|s2)  #union
print(s1-s2)    #difference
print(s1^s2)  #Symmetric_difference












