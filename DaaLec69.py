"""
OOPs:Object Oriented Programming
class,object

Main Pillars:Encap,Abstraction,Inheritance,Polymorphism

Inheritance: A child class's object can access parent class's properties

class Parent:
    def fun1(self):
        print("I am fun1 in class Parent")
class Child(Parent):
    def fun2(self):
        print("I am fun2 in class Child")
class myclass(Child,Parent):
    def fun3(self):
        print("I am fun3 in class myclass")
obj=myclass()
obj.fun1()

Polymorphism (Poly=Many + morphism=forms)
-function overloading
-function overriding

#function overloading
class Demo:
    def add(self,a,b):
        return a+b

obj=Demo()
print(obj.add(10,20))   #addition
print(obj.add('Aman','Kumar'))  #Concatenation
print(obj.add([1,2,3],[4,5,6]))  #Extend


"""

#function Overiding

class A:
    def fun(self):
        print("I am in class A")
class B(A):
    def fun(self):
        print("I am in class B")

obj=B()
obj.fun()   #this object will use its own Property

#Abstraction
