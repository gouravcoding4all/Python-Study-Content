"""
Tuple:-Tuple is also a collection of hetreogenous elements like LIST.
tuple_name=(val1,val2,val3...)

ways to create a tuple
t=(23,43,566,78,90,23)
t=(23,45,67,'Aman',True,2+7j)
t=()
t=tuple([23,54,56,67,78])
t=tuple((23,54,56,67,78))
t=tuple()
print(t)
print(type(t))

Tuple works on Index
forward(0,1,2,3...)
backward(-1,-2,-3..
         tuple_name[index]

t=(23,43,566,78,90,23)
print(t)
print(t[2])
print(t[-4])

Tuple can be Sliced
tuple_name[start:stop:step]
t=(23,43,566,78,90,23)
print(t)
print(t[2:5:1])
print(t[2:5])
print(t[-4:-1])
print(t[-2:-5:-1])

Tuple support Replication

t=(1,2,3,4,5)
print(t)
print(t*3)

Tuple can be Traverse/Iterration
t=(23,34,56,78,89,74,32)
print(t)
for x in t:
    print(x)
print(t*3)

t=(23,34,56,78,89,74,32)
print(t)
print(sum(t))
print(max(t))
print(min(t))
print(len(t))

Iteration / traversing using while loop

t=(23,34,45,67,89,90,34)
print(t)
i=0
while i<len(t):
    print(t[i])
    i=i+1

Tuple's Method
count,index

t=(23,67,12,67,34,23,32,67)
print(t)
print(t.count(67))
print(t.index(12))
print(t.index(34))
#print(t.index(34,5))

Tuple is immuteable (you can not change anything)
List is muteable (changeable)

li1 = (1,2,3)
li2 = (1,2,3)
print(li1 is li2)   # True

t1[1].append(44)
print(t1)

"""

t1 = (23,[11,22,33],54,56)
t2 = (23,[11,22,33],54,56)
print( t1 is t2 )  # False (tuple has muteable object)

    
t1[1].append(44)
print(t1)
