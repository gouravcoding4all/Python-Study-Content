"""
match case
var = int(input("Enter a number:"))
match var:
    case 1:
        print("I am in case 1")
    case 2:
        print("I am in case 2")
    case 3:
        print("I am in case 3")
    case _:
        print("No match with any case")

#wap to calculate the gross salary of an employee where HRA is 20% and DA
        is 30% if basic salry is under 10001 and HRA 30% and DA 40% if basic salary
        is under 30001 and above 30000 HRA 35% and DA is 45%
        Hint:-GrossSalary=Basic_Salary + HRA + DA
bs = float(input("Enter Basic Salary:"))
match bs:
    case bs if bs<10001:
        hra=bs*0.20
        da=bs*0.30
    case bs if bs<30000:
        hra=bs*0.20
        da=bs*0.30
    case _:
        hra=bs*0.35
        da=bs*0.45
gs=bs+hra+da
print("Gross Salary:",gs)

#while Loop:-
#initialization
#while condition:
#    statement
#    incr/decr
#Example:
a=1
while a<=5:
    print("Hello")
    a+=1

#find factorial of a number entered by user.
#factorial=>5->5*4*3*2*1=>120
num=int(input("Enter a Number: "))
fact = 1
a = 1
while a<=num:
    fact=fact*a
    a=a+1
print("Factorial : ",fact)

#Wap to add digits of a number
num=28356
add=0
while num>0:
    rem=num%10 #1
    add= add+rem #6
    num=num//10 #0
print("Total of Digits:",add)
#----------
num=int(input("Enter A number: "))
add=0
while num>0:
    rem=num%10 #1
    add= add+rem #6
    num=num//10 #0
print("Total of Digits:",add)

#Reverse a number using while loop
num=int(input("Enter A number: "))
add=0
while num>0:
    rem=num%10 
    add= add*10+rem 
    num=num//10 
print("Total of Digits:",add)

#Reverse a number using while loop
num=int(input("Enter A number: "))
print(str(num)[::-1])

#create a number guessing game:
#Generate a random number(1-10)
#keep asking user until they guess correctly
import random
print(random.random())

import random
print(random.randint(1,5))

"""

import random
num=random.randint(1,5)
while True:
    guess=int(input("Guess Number from 1 to 5: "))
    if num==guess:
              print("You Guess Right Number was :",num)
              break
    else:
              print("No,Guess Again!")
































