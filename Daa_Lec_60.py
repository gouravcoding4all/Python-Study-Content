"""
Error:-A mistake in your code.
Types of error:-
1-syntax Error
A type or a mistake in your syntax is called syntax Error.
This error will flag by compiler/interpreter  and it will not let you to run the
program.

print("hell India')
You need to fix this error,to run the program
without fixing you can not run or by pass or handle the error

2- Runtime error
A mistake in your logic thats why its also called logical error
This type of error can not flag by interpreter and it will let you run the program.
a=int(input("Enter A Number: "))
b=int(input("Enter B Number: "))
print("Division :",a/b)

Denominator should not be zero
It will raise an Exception/Runtime Error and it will crash the program.
This type of error can be bypass and handle it at runtime
this process is called Exception Handling

3- Symmetric Error:
This type of error do not flag by interpreter and they will not crash  the program
You will not get the desired output in this situation
a=int(input("Enter A Number : "))
b= int(intput ("Enter B Number : "))
print("Addition : ",a*b)  #it should be + sign
you need to find the bug and fix it.
you can not bypass or handle.

Exception Handling:
try,except,finally

try:
    write your code here where you have a doubt
except:
    Alternate code

print("Start Program")
a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
print("Division :",a/b)
print("End Program")
"""

print("Start Program")
a = int(input("Enter A Number : "))
b = int(input("Enter B Number : "))
try:
    print("Division :",a/b)
except:
    print("Cannot divide by zero")
print("End Program")



print("Start Program")

try:
    a = int(input("Enter A Number : "))
    b = int(input("Enter B Number : "))
    print("Division :",a/b)
except:
    print("Division is not possible")
print("End Program")



