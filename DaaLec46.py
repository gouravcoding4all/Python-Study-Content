Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
Operators
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    Operators
NameError: name 'Operators' is not defined
"""Operators
a+b=>(a,b) Operands , (+) Operator
Operator operates on operands

1)Arithmetic Operators
+,-,*,/,%,//,**

a=7
b=5
print(a+b)  #12
print(a-b)  #2
print(a*b)  #35
print(a/b)  #1.4
print(a%b)  #% modulus(to calculate the remainder)
print(11%4) #3
print(a//b) #// floor division/truncation(it divides but it removes the decimal/point value)
... print(11//4)#2
... print(2**5) #** Exponential(To calculate the power)
... print(5**3) #5 to the power 3 (5*5*5)
... 
... 2)Assignment Operator
... =,+=,-=,*=,/=,etc.
... a=10 #a is assign to 10
... a+=1 #a=a+1
... a*=2 #a=a*2
... a/=5 #a=a/5
... print(a)
... 
... 3)Relational/Conditional Operators
... >,<,>=,<=,==,!=  (return boolean answers)
... Boolean =true/false
... 
... a=7
... b=5
... print(a>b)
... print(a<b)
... print(a>=b)
... print(a<=b)
... print(a!=b) #is not equal to
... print(a==b) #is equal to
... 
... 4)Membership Operator(Check Existance)
... in, not in (Return Boolean Answer)
... a='aman'
... b='amankumar'
... print(a in b)
... print('ankum' in b)
... print('ka' in b)
... print('ka' not in b)
... 
... a=[1,2,3]
... b=[1,2,3]
... print(a in b) #False
... 
... a=[1,2,3]
... b=[1,2,[1,2,3],3]
... print(a in b) #True
