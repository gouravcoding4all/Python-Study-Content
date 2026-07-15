"""
while LOOp:-execute a same task again for a finite times
syntax:-
initiazation
while condition:
statements
inc/dec
Example:-

a=1
while a<5:
        print("Hello")
        a=a+1

a=1
while a<=5:
    print(a)
    a=a+1

#Print counting from 1 to 10
a=1
while a<=10:
    print(a)
    a=a+1

#Print counting from 1 to N
n=int(input("Enter Number: "))
a=1
while a<=10:
    print(a)
    a=a+1

#Print Table of a Number:
n=int(input("Enter Number: "))
a=1
while a<=10:
    print(a*n)
    a=a+1

#Print all factors of a number
#Number HINT:- 12 => 1,2,3,4,6,12
n=int(input("Enter Number: "))
a=1
while a<n:
    if n%a==0:
        print(a)
    a=a+1

#Count factors of a number
count=0
n=int(input("Enter Number: "))
a=1
while a<=n:
    if n%a==0:
        print(a)
        count+=1
    a=a+1
print("Total Factors : ",count)

#Wap to check a number is prime or not
count=0
n=int(input("Enter Number: "))
a=1
while a<=n:
    if n%a==0:
        count+=1
    a=a+1
if count==2:
    print("Prime")
else:
    print("Not Prime")

#Wap to check a number is prime or not
count=0
n=int(input("Enter Number: "))
a=1
while a<=n:
    if n%a==0:
        count+=1
    a=a+1
if count==2:
    print("Prime")
else:
    print("Not Prime")

#keywords
#break,continue,pass,else

#break:-break will exit from the current loop
a=1
while a<=7:
    if a==4:
        break
    print(a)
    a=a+1

#continue:-will take the cursor to the loop again
a=1
while a<=7:
    if a==4:
        continue
    print(a)
    a=a+1

#pass:-pass will pass the cursor to the next line
a=1
while a<=7:
    if a==4:
        pass
    print(a)
    a=a+1

"""

#else
a=1
while a<=3:
    if a==4:
        break
    print(a)
    a=a+1
else:
    print("Hello")
------------------
a=1
while a<=7:
    if a==4:
        break
    print(a)
    a=a+1
else:
    print("Hello") 
