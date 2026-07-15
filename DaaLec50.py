"""
Looping :- Loop is use to execute a task again n again for a finite times.
types of loop:
for and while

for
syntax:-
for variable_name in range(start_value,stop_value,step_value):
statements

print(*range(1,10,1))

Example:-
for a in range(1,10,2):
print("Hello")

for a in range(1,10,2):
    print(a)

for a in range(1,11,3):
    print(a)
    
#By default step=1
for a in range(1,11):
    print(a)

#By default step=1
for a in range(5,9):
    print(a)

#By default step=1
#By default start=0
for a in range(5):
    print(a)

#By default step=1
#By default start=0
for a in range():   #error:-at least one argument required
    print(a)

#WAP to print counting from 1 to 10
for i in range(1,11):
    print(i)

#WAP to print counting from 1 to N
n=int(input("Enter A Number: "))
for i in range(1,n+1):
    print(i)


#WAP to print table of a number
n=int(input("Enter A Number: "))
for i in range(1,11):
    print(i*n)

#WAP to print table of a number
#format=> 5*1=5
n=int(input("Enter A Number: "))
for i in range(1,11):
    print(n,"*",i,"=",i*n)

#WAP to print table of a number
#Hint:- 12=>1,2,3,4,6,12 
n=int(input("Enter A Number: "))
for i in range(1,n+1):
    if n%i==0:
        print(i)

#WAP to print table of a number
#Hint:- 12=>1,2,3,4,6,12
count=0
n=int(input("Enter A Number: "))
for i in range(1,n+1):
    if n%i==0:
        count=count+1
print("Total Factors:",count)

count = 0
n = int(input("Enter A Number: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        count = count + 1

print("Total Factors:", count)

#WAP to cheack a number is prime
count=0
n=int(input("Enter A Number : "))
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print("Prime")
else:
    print("Not Prime")
    
#Keywords
break,continue,pass

#break:-It will exit from the current loop

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    print(i)
    if i==5:
        break

for i in range(1,11):
    if 6%i==0:
        break
    print(i)

for i in range(1,11,3):
    if i%7==0:
        break
    print(i)

#continue:- continue will take the cursor to the loop again
#continue will not execute the next code
for i in range(1,11,3):
    if i%2==0:
        break
    print(i)

for i in range(1,11,3):
    if i%2==0:
        break
    print(i)

#continue:-
for i in range(1,11):
    if i==6:
        continue
    print(i)

for i in range(1,11):
    print(i)
    if i%2==0:
        continue

#Pass:- pass do nothing
#pass just pass the cursor to the next line
for i in range(1,11):
    if i==5:
        pass
    print(i)


"""

if 10>5:
    pass
print("Hello")



