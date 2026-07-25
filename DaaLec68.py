"""
find all palindromes from a list using filter

li = ['Raman', 'Madam', 'Naman', 'Rohan', 'Mam', 'Ram']
checkPalindrome = lambda val: val.lower() == val.lower()[::-1]
res = list(filter(checkPalindrome, li))
print(res)

def checkPalindrome(val):
    start = 0
    end = len(val) - 1
    while start < end:
        if val[start].lower() != val[end].lower():
            return False
        start += 1
        end -= 1

    return True

li = ['Raman', 'Madam', 'Naman', 'Rohan', 'Mam', 'Ram']
res = list(filter(checkPalindrome, li))
print(res)
-------
checkPalindrome=lambda val: val==int(str(val)[::-1])
li=[346,675,121,454,688,989,452]
res=list(filter(checkPalindrome,li))
print(res)

def checkPalindrome(num):
    copy=num
    rev=0
    while num>0:
        rem=num%10
        rev=rev*10+rem
        num=num//10
    return rev==copy

li=[346,675,121,454,688,989,452]
res=list(filter(checkPalindrome,li))
print(res)

Oops:Object Oriented Programming
class,Obect
Encapsulation,Polymorphism,Abstraction,Inheritance

class:class is a virtual entity
class is the blue print of an object
class is the representation of encapsulation

Syntax:-
class class_name:
    class's properties
    data member(variable)
    member function(methos)

class myclass:
    a=100
    def greet():
        print("Good Morning!")

Object: Object is the real entity
Object is the instance of an class
-------------
class myclass:
    a=100
    def greet():
        print("Good Morning!")

print(myclass.a)
myclass.greet()

class myclass:
    a=100
    def greet():
        print("Good Morning!")

print(myclass.a)
myclass.greet()
myclass.a=200
print(myclass.a)

class myclass:
    a=100
    def greet():
        print("Good Morning!")

obj1=myclass()
obj2=myclass()
print(obj1.a)
obj1.a=90
print(obj1.a)
print(obj2.a)

#self:self is current class's object
class myclass:
    a=100
    def greet(self):
        print("Good Morning!")

obj=myclass()
obj.greet()
    
 #self:self is current class's object
class myclass:
    a=100
    def greet(self,var):
        print("value of var is ",var)
        print("value of a is",self.a)
            
obj=myclass()
obj.greet(20)
    
Constructor: Constructor is a property of a method where this method called automatically when an object will be created
#or

Constructor in Python (Simple Definition)
A constructor is a special function that runs automatically when we create an object of a class. It is used to give initial values to the object.

#Even Simpler Definition
A constructor is a special method that automatically starts working when a new object is created. It helps prepare the object for use.
   
"""

class myclass:
    a=100
    def myfun(self):
        print("Hello India")
    def __init__(self):
        print("I am a constructor")

obj=myclass()



