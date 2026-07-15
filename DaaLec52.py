"""
Pattern Programming

*****
*****
*****
*****
*****

print("*****\n"*5)

for i in range(5):
    print("*****")

for i in range(5):
    print("*"*5)
------------------------------------------------------
    
*
**
***
****
*****    
for i in range(1,6):
    print("*"*i)
------------------------------------------------------
1
12
123
1234
12345
st=""
for i in range(1,6):
    st=st+str(i)
    print(st)

st = ""

for i in range(1,6):
    st = st + str(i)
    print(st)
Step 1: st = ""

Socho tumhare paas ek khali box 📦 hai.

st = ""

Is box ke andar kuch bhi nahi hai.

st = ""
Step 2: for i in range(1,6):

Ye bolta hai:

1 se 5 tak counting chalao.

To i ki value ek-ek karke hogi:

1
2
3
4
5
Step 3: Sabse Important Line
st = st + str(i)

Iska matlab hai:

👉 Purane st ke andar naya number jod do.

str(i) ka matlab:

Number ko text (string) bana do.

1st Time Loop

i = 1

Pehle:

st = ""

Ab:

st = "" + "1"

Result:

st = "1"

Print hoga:

1
2nd Time Loop

i = 2

Pehle:

st = "1"

Ab:

st = "1" + "2"

Result:

st = "12"

Print:

12
3rd Time Loop

i = 3

Pehle:

st = "12"

Ab:

st = "12" + "3"

Result:

st = "123"

Print:

123
4th Time Loop

i = 4

Pehle:

st = "123"

Ab:

st = "123" + "4"

Result:

st = "1234"

Print:

1234
5th Time Loop

i = 5

Pehle:

st = "1234"

Ab:

st = "1234" + "5"

Result:

st = "12345"

Print:

12345
Final Output
1
12
123
1234
12345
Easy Example 🍫

Socho tum chocolates collect kar rahe ho.

Pehle:

📦 Empty Box

Fir:

1 🍫

Fir doosri chocolate add ki:

1🍫 2🍫

Fir teesri:

1🍫 2🍫 3🍫

Fir chauthi:

1🍫 2🍫 3🍫 4🍫

Fir paanchvi:

1🍫 2🍫 3🍫 4🍫 5🍫

Har baar purani chocolates nahi hat rahi hain, sirf ek nayi chocolate add ho rahi hai. Bilkul waise hi st har loop me bada hota ja raha hai.

Yaad Rakhne ki Trick 🧠
st = Purana st + Naya Number

Jaise:

""     + "1" = "1"
"1"    + "2" = "12"
"12"   + "3" = "123"
"123"  + "4" = "1234"
"1234" + "5" = "12345"
Ek line me:

st ek bag ki tarah hai. Har loop me us bag me ek naya number add hota hai, isliye output har baar bada hota jata hai. 🚀

---------------------------------------------
1
22
333
4444
55555
for i in range(1,6):
    print(str(i)*i)
------------------------------------
A
AB
ABC
ABCD
ACBDE

st=""
for i in range(1,6):
    st=st+chr(i+64)
    print(st)
-----------------------------------
    *
   **
  ***
 ****
*****
for i in range(1,6):
    print(" "*(5-i)+"*"*i)

-----------------------------------------
0
909
89098
7890987
678909876
56789098765
4567890987654
345678909876543
23456789098765432
1234567890987654321


"""
st="0"
for i in range(10,0,-1):
    if i!=10:
        st=str(i) + st + str(i)
    print(st)

