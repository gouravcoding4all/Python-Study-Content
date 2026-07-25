"""
Advance Python
    lambda,,map,filter,reduce
    OOPs:- Class,Objects
    4 Main Pillars: Encapsulation,Inheritance,Polynomial,Abstract

def cube(num):
    return num**3

print(cube(4))
    
Lambda:-Lambda is use to write definition of a function or it is ude to write a small definition function mostly a single functions.

function_name=Lambda parameter:definition

cube=lambda num:num**3
print(cube(4))
print(cube(2))

checkEven=lambda num: 'Even' if num%2==0 else 'odd'
print(checkEven(18))
print(checkEven(15))

checkpositive=lambda num:'Positive' if num>0 else 'Negative' if num<0 else 'Zero'
print(checkpositive(17))
print(checkpositive(-45))
print(checkpositive(0))

cube=lambda num:num**3

#li=[x for x in range(1,11)] #list comprehension
li=[1,2,3,4,5,6,7,8,9,10]
print(li)

for m in li:
    print( cube(m))

#Map: Map is a function which is use to apply a function/method on collection without traversion/itteration.

#map() function in Python is a built-in tool that applies a specific function to all items in an iterable (like a list or tuple) and returns a lazy map iterator object

cube=lambda num:num**3
li=[1,2,3,4,5,6,7,8,9,10]
print(li)

res=list(map(cube,li))
print(res)

findEven = lambda num: True if num % 2 == 0 else False

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(li)

for m in li:
    if findEven(m):
        print(m)
#or
findEven = lambda num: num % 2 == 0

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for m in li:
    if findEven(m):
        print(m)      

#Filter
#filter is a method/function which is use to apply a function on a collection without itteration to collect required elements.
findEven = lambda num : True if num%2==0 else False
li=[1,2,3,4,5,6,7,8,9,10]
print(li)
res=list(filter(findEven,li))
print(res)

add=lambda a,b : a+b
li = [1,2,3,4,5,6,7,8,9,10]
res=0
for m in li:
    res = res+m
print(res)

#Reduce:Reduce is use to apply a method  on a collection without itteration to calculate a value
from functools import reduce
add=lambda a,b:a+b
li=[1,2,3,4,5,6,7,8,9,10]
res=reduce(add,li)
print(res)

#Reduce:Reduce is use to apply a method  on a collection without itteration to calculate a value
from functools import reduce
add=lambda a,b:a+b
li=[1,2,3,4,5,6,7,8,9,10]
res=reduce(add,li)
print(res)

#Wap to add square of all even number from a list
from functools import reduce
checkEven = lambda num:num%2==0
findSquare=lambda num : num**2
findAdd=lambda a,b:a+b
li=[23,67,98,36,42,78,79,35,67]
even=filter(checkEven,li)
square=map( findSquare,even)
add=reduce(findAdd,square)
print(add)

from functools import reduce
checkEven = lambda num:num%2==0
findSquare=lambda num : num**2
findAdd=lambda a,b:a+b
li=[23,67,98,36,42,78,79,35,67]
even=list(filter(checkEven,li))
print(even)
square=list(map( findSquare,even))
print(square)
add=reduce(findAdd,square)
print(add)

"""

li=[1,2,3,4,5,6,7,8,9,10]
#Anonymous Function
res = list(filter(lambda num:num%2==0,li))
print(res)

#Anpnymous Function
#Anonymous List
print(list(filter(lambda num:num%2==0,[1,2,3,4,5,6,7,8,9,10])))

from functools import reduce
print(reduce(lambda a,b:a+b,map(lambda num:num**2,filter(lambda num:num%2==0,[23,34,45,56,67,89,90]))))






