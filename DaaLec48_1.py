"""
for a in range(1,11,1):  
    print(a)

Looping:- Loop is technique by which you can execute a same task agin n again.
There are two ways to apply loop
for Loop and while Loop

for
syntax:-
for variable_name in range(start,stop,step):
statements
print(*range(1,10,2))
print(*range(1,10,1))
print(*range(1,10,3))
"""

""" for a in range(1,5,1):
    print("Hello")

for a in range(1,5,1):
    print(a)

for a in range(1,11,1):
    print(a)

for a in range(1,11,2):
    print(a)

#by default step=1
    for a in range(1,11):
        print(a)

#by default step=1
    for a in range(5,9):
        print(a)

#by default step = 1
#by default start = 0
for a in range(5):
    print(a)

#WAP to print counting from 1 to 10
    for i in range(1,11):
        print(i)

#WAP to print counting from 1 to N
        n=int(input("Enter A Number : "))
        for i in range(1, n+1):
            print(i)

#WAP to print table  of a number
num=int(input("Enter A NUMBER : "))
for i in range(1,11):
    print(i*num)

#WAP to print all factors of a number
  #  HINT:- 12=>1,2,3,4,6,12 => 6 factors

    #count = 0

"""
n = int(input("enter a number : "))
    for i in range(1,n+1):
        if n%i==0:
            print(i)
            

# WAP to print all factors of a number
HINT:-   12 =>  1,2,3,4,6,12
n = int(input("Enter A Number : "))
for i in range(1,n+1):
    if n%i==0:  
        print(i)


# WAP to count the factors of a number
HINT:-   12 =>  1,2,3,4,6,12   =>   6 factors

count = 0
n = int(input("Enter A Number : "))
for i in range(1,n+1):
    if n%i==0:   
        print(i)
        count = count+1 
print("Total Factors :",count)

# WAP to check a number is Prime
# A number which has exactly 2 factors

count = 0
n = int(input("Enter A Number : "))
for i in range(1,n+1):
    if n%i==0:   
        print(i)
        count = count+1 
print("Total Factors :",count)
if count==2:
    print("Prime")
else:
    print("Not Prime")

    
# break , continue , pass

# break:- it will break from the current loop
# break will exit from the current loop

for i in range(1,11):
    if i==4:
        break
    print(i)


# break:- it will break from the current loop
# break will exit from the current loop

for i in range(1,11):
    print(i)
    if i==4:
        break



# break:- it will break from the current loop
# break will exit from the current loop

for i in range(1,11):
    print(i)
    if i%5==0:
        break


for i in range(1,11):
    if i%5==0:
        break
    print(i)
















    
