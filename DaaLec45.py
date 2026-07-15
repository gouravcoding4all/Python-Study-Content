Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#single Line Comment
"""
Multiline Comment
Built-in Functions:-
print , input ,int ,float , type

PRINT:-It is use to display a message on console screen.

print('Hello Goa')
print("Hello India")
print('''Hello Mumbai''')
print('''Aman is my younger brother''')
a=10
print('a')  #as it as
print(a)    #value of a variable
print("hello a")
print("hello",a)
a=10
b=20
print('Value of a is ',a,' and of b is',b)
print(f'Value of a is {a} and value of b is {b}')

INPUT:-input is a function which is  use to ask value from user input function always return a string/text value.

a=input("Enter A Number : ")
b=input("Enter B Number : ")
c=a+b
print("Addition:",c)  #Concatenation

INT:-int is a function which is use to convert a value into numeric (do not support point/decimal value)

a= int(input("Enter A Number : "))
b= int(input("Enter B Number : "))
c=a+b
print("Addition :",c)

FLOAT:-Float is use to convert a value into numeric(also support Point/decimal value)

a=float(input("Enter A  Number : "))
b=float(input("Enter  B Number : "))
c=a+b
print("Addition :",c)

TYPE:-type is use to show the data type of a variable
Python is a Dynamic programming language
a=29
print(type(a))
a=29.65
print(type(a))
a='Aman'
print(type(a))
a=2+9j
print(type(a))

#WAP to claculate the gross salary of a employee where HRA is 20% and DA is 30% of his basic Salary.
HINT:-Gross Salary = Basic Salary + HRA + DA
"""
'\nMultiline Comment\nBuilt-in Functions:-\nprint , input ,int ,float , type\n\nPRINT:-It is use to display a message on console screen.\n\nprint(\'Hello Goa\')\nprint("Hello India")\nprint(\'\'\'Hello Mumbai\'\'\')\nprint(\'\'\'Aman is my younger brother\'\'\')\na=10\nprint(\'a\')  #as it as\nprint(a)    #value of a variable\nprint("hello a")\nprint("hello",a)\na=10\nb=20\nprint(\'Value of a is \',a,\' and of b is\',b)\nprint(f\'Value of a is {a} and value of b is {b}\')\n\nINPUT:-input is a function which is  use to ask value from user input function always return a string/text value.\n\na=input("Enter A Number : ")\nb=input("Enter B Number : ")\nc=a+b\nprint("Addition:",c)  #Concatenation\n\nINT:-int is a function which is use to convert a value into numeric (do not support point/decimal value)\n\na= int(input("Enter A Number : "))\nb= int(input("Enter B Number : "))\nc=a+b\nprint("Addition :",c)\n\nFLOAT:-Float is use to convert a value into numeric(also support Point/decimal value)\n\na=float(input("Enter A  Number : "))\nb=float(input("Enter  B Number : "))\nc=a+b\nprint("Addition :",c)\n\nTYPE:-type is use to show the data type of a variable\nPython is a Dynamic programming language\na=29\nprint(type(a))\na=29.65\nprint(type(a))\na=\'Aman\'\nprint(type(a))\na=2+9j\nprint(type(a))\n\n#WAP to claculate the gross salary of a employee where HRA is 20% and DA is 30% of his basic Salary.\nHINT:-Gross Salary = Basic Salary + HRA + DA\n'
>>> bs=float(input("Enter Basic Salary: "))
Enter Basic Salary: 
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    bs=float(input("Enter Basic Salary: "))
ValueError: could not convert string to float: ''
>>> hra=bs*0.20
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    hra=bs*0.20
NameError: name 'bs' is not defined. Did you mean: 'abs'?
>>> 
>>> da=bs*0.30
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    da=bs*0.30
NameError: name 'bs' is not defined. Did you mean: 'abs'?
>>> gs=bs+hra+da
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    gs=bs+hra+da
NameError: name 'bs' is not defined. Did you mean: 'abs'?
>>> print("Gross Salary:",gs)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print("Gross Salary:",gs)
NameError: name 'gs' is not defined
>>> bs=float(input("Enter Basic Salary: "))
... hra=bs*0.20
... da=bs*0.30
... gs=bs+hra+da
... print("Gross Salary:",gs)
... 
SyntaxError: multiple statements found while compiling a single statement
>>> bs=float(input("Enter Basic Salary: "))
Enter Basic Salary: 100000
>>> hra=bs*0.20
>>> da=bs*0.30
>>> gs=bs+hra+da
>>> print("Gross Salary:",gs)
Gross Salary: 150000.0
