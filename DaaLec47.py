Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
"""
python Operators
5.Identity Operator(Exact Match (check Memory))
is , is not (Return Boolean Answer)
"""
a="aman"
b="amankumar"
c="aman
print(a is b)                                                                                   
[DEBUG ON]
[DEBUG OFF]
"""
python Operators
5.Identity Operator(Exact Match (check Memory))
is , is not (Return Boolean Answer)
"""
a="aman"
b="amankumar"
c="aman
print(a is b)
SyntaxError: multiple statements found while compiling a single statement
print(a is b)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(a is b)
NameError: name 'a' is not defined
a="aman"
b="amankumar"
c="aman"
print(a is b)
False
print(a is c)
True
print(a is not b)
True
"""
python Operators
5.Identity Operator(Exact Match (check Memory))
is , is not (Return Boolean Answer)
"""
a="aman"
b="amankumar"
c="aman
print(a is b)"""
python Operators
5.Identity Operator(Exact Match (check Memory))
is , is not (Return Boolean Answer)
"""
a="aman"
b="amankumar"
c="aman
print(a is b)
SyntaxError: multiple statements found while compiling a single statement
"""Logical Operatoor
and ,or,not
and:-if both/
all input are True,then result is True otherwise False
"""
'Logical Operatoor\nand ,or,not\nand:-if both/\nall input are True,then result is True otherwise False\n'
print(10>5 and 10<5)
False
print(10>5 and 7>4)
True
print(10>50 and 10<5)
False
"""or:-if both/all inputs are False,then result is False otherwise True"""
'or:-if both/all inputs are False,then result is False otherwise True'
print(10>5 or 7>4)
True
print(10>5 or 10<5)
True
print(10>5 or 1o<50)
SyntaxError: invalid decimal literal
print(10>5 or 10<50)
True
print(10>50 or 10<5)
False

"""not:- Not operator is also called invertor gate/operator
not works with only one input
if the input is True, OUTPUT will be False and vice-versa.
"""
'not:- Not operator is also called invertor gate/operator\nnot works with only one input\nif the input is True, OUTPUT will be False and vice-versa.\n'
print(not 10>5)
False
a=7
b=5
print(a and b)
5
print(int(True)) #1
1
print(int(False)) #0
0
print(bool(0))
False
print(bool())
False
print(bool(false))
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    print(bool(false))
NameError: name 'false' is not defined. Did you mean: 'False'?
print(bool(None))
False
print(bool(1))
True
print(bool(235547))
True
print(bool(-456.567))
True
print(bool("aman"))
True
a=7
b=5
print(a and b)  #5
5
print(b and a)  #7
7
a=7
b=0
print(a or b)
7
print(b or a)
7
print(not 34)  #retuen boolean  Answer
False
a=7
b=0
print(a and b) #0
0
print(b and a) #0
0
>>> a=7
>>> b=5
>>> print(a or b)
7
>>> print(b or a)
5
>>> print(True + True * False)
1
>>> #1+1*0
>>> #1+0
>>> #1
>>> 
>>> print(10>20 + 20>50)
False
>>> #10>20 + 20>50   #+ has higher precedence compare to relational operator
>>> #10>40>50
>>> #10>40 and 40>50
>>> #False and False
>>> #False
>>> 
>>> #PEMDAS
>>> #PARANTHESIS()
>>> #EXPONENTIAL **
>>> MULTIPLICATION
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    MULTIPLICATION
NameError: name 'MULTIPLICATION' is not defined
>>> #MULTIPLICATION
>>> #DIVISION
>>> #ADDITION
>>> #SUBTRACTION
>>> 
>>> a=5
>>> b=10
>>> print(a<b<20)
True
>>> #a<b<20
>>> #a<b and b<20
>>> #True and True
