"""
For Looping
else keyword

for i in range(1,11):
    print(i)
else:
    print(0)

else will work  after for loop

for i in range(1,11):
    if i==5:
        continue
    print(i)
else:
    print(0)

for i in range(1,11):
    if i==5:
        break
    print(i)
else:
    print(0)

#Nested Loop
#WAP to check a number is Prime or Not
num=18
count=0
for i in range(1,num+1):
    if num%i==0:
        count+=1
        
if count==2:
    print(num,"is Prime")
else:
    print(num,"is Not Prime")

#WAP to find all prime number from 1 to 50
for num in range(1,51):
        count=0
        for i in range(1,num+1):
            if num%i==0:
                count+=1
        if count==2:
            print(num)

#Pattern Programming
*****
*****
*****
*****
*****

print("*****")
print("*****")
print("*****")
print("*****")
print("*****")

print("*****\n*****\n*****\n*****\n*****")

print("*****\n"*5)

for i in range(5):
    for j in range(1,6):
        print("*",end='')
    print()

for i in range(5):
    print("*****")

for i in range(1,6):
    for j in range(1,6):
        print("*",end=' ')
    print()
-----------------------------------
*
**
***
****
*****
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=' ')
    print()
--------------------------------------
1
12
123
1234
12345

for i in range(1,6):   
    for j in range(1,i+1):  
        print(j,end="")
    print()
--------------------------------------------------------
1
22
333
4444
55555
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
------------------------------
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
------------------------------------
1 
2 3 
4 5 6 
7 8 9 10 
k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end=' ')
        k+=1
    print()
-----------------------------------------------
A
AB
ABC
ABCD
ABCDE
k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+64),end=' ')
        k+=1
    print()
--------------------------------------
a
ab
abc
abcd
abcde
k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(j+96),end=' ')
        k+=1
    print()

#A=65
#a=97
#Z=90
#z=122
-----------------------------
1
01
010
1010
10101
k=1
m=-1
for i in range(1,6):
    for j in range(1,i+1):
        print(k,end=' ')
        k=k+m
        m=-m
    print()
    
Explaination:
Step 1: Do Boxes Socho 📦
k = 1   ← Ye number print hoga.
m = -1  ← Ye batata hai ki next time 1 ghatana hai ya 1 badhana hai.

Har baar:

Agar m = -1 hai → k se 1 ghatao.
Agar m = 1 hai → k me 1 jodo.

Aur phir:

m = -m

Ye m ka sign ulta kar deta hai.

-1 → 1
1 → -1

Isliye program baar-baar +1 aur -1 karta rehta hai.

Step 2: Pehli Line

Shuru me:

k = 1
m = -1

Print:

1

Ab:

k = 1 + (-1) = 0
m = 1
Step 3: Dusri Line

Ab:

k = 0
m = 1

Print:

0

Update:

k = 0 + 1 = 1
m = -1

Phir print:

1

Update:

k = 1 + (-1) = 0
m = 1

Dusri line:

0 1
Step 4: Teesri Line

Shuru:

k = 0
m = 1

Print:

0

Update:

k = 1
m = -1

Print:

1

Update:

k = 0
m = 1

Print:

0

Teesri line:

0 1 0
Isi tarah aage

Output:

1
0 1
0 1 0
1 0 1 0
1 0 1 0 1
Ek Chhoti Story 🎮

Socho ek game hai jisme ek robot ke paas sirf 2 buttons hain:

🔴 Button 1 → Number ko 1 kam karo.
🟢 Button 2 → Number ko 1 zyada karo.

Robot har print ke baad button badal deta hai.

Start → 1

Print 1
↓ (-1)
0
↓ (+1)
1
↓ (-1)
0
↓ (+1)
1
↓ (-1)
0

Isliye numbers hamesha:

1 → 0 → 1 → 0 → 1 → 0 ...

banate rehte hain.

Yaad rakhne ki Trick ⭐
k = jo number print hoga.
m = batata hai +1 karna hai ya -1.
m = -m = button change (minus se plus, plus se minus).

Isliye k kabhi 1, kabhi 0, kabhi 1, kabhi 0 banta rehta hai.
------------------------------------
1 
0 1 
0 1 0 
1 0 1 0 
1 0 1 0 1 
k=1
for i in range(1,6):
    for j in range(1,i+1):
        print(k%2,end=' ')
        k=k+1
    print()
--------------------------------------
    *
   **
  *** 
 ****
*****
for i in range(1,6):
    for k in range(i,5):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=' ')
    print()
------------------------------------
    *
   ***
  *****
 *******
*********


    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *


    *
   ***
  *****
 *******
*********
 ****
  ***
   **
    *


    *
   ***
  *****
 *******
*********
 ***
  **
   *


    *
   ***
  *****
 *******
****
 ***
  **
   *

    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *


    *
   ***
  *****
 *******
*********
    ****
    ***
    **
    *


    *
   ***
  *****
 *******
    *****
    ****
    ***
    **
    *


    *    
    **
    ***
    ****
    *****
    ****
    ***
    **
    *


     *
     **
     ***
     ****
     ***
     **
     *


    *
   **
  ***
 ****
*********
 *******
  *****
   ***
    *


    
   *
  **
 ***
*********
 *******
  *****
   ***
    *


    *
   **
  ***
 ****
*****
 *******
  *****
   ***
    *
"""

for i in range(1,6):
    for k in range(i,5):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=' ')
    print()


