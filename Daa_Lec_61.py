"""
Exception Handling
    try,except ,finally

try:
    doubtful code
except:
    alternate code
finally:
    execute always

---
print("Start Program")
a=int(input("Enter A Number : "))
b=int(input("Enter B Number : "))
try:
    print("Division :",a/b)
except:
    print("Division is not possible")
finally:
    print("It will always execute")
print("Program End!")
---
try:
    a=int(input("Enter A Number : "))
    b=int(input("Enter B Number : "))
    print("Division :",a/b)
except:
    print("Division is not Possible")
print("Program End!")
--------
print("Start Program")
try:
    a=int(input("Enter A Number : "))
    b=int(input("Enter B Number : "))
    print("Division :",a/b)
except ZeroDivisionerror as e:
    print("Error:",e)
print("Program End!")
-------------

#Nested Except Block:-
print("Start Program")
try:
    print("Start Program")

    try:
        a = int(input("Enter A Number: "))
        b = int(input("Enter B Number: "))
        print("Division:", a / b)

    except ZeroDivisionError as e:
        print("Error:", e)

    except ValueError as e:
        print("Error:", e)

except Exception as e:
    print("Outer Error:", e)

print("Program End!")
------------------
print("Start Program")

try:
    try:
        a = int(input("Enter A Number: "))
        b = int(input("Enter B Number: "))
        print("Division:", a / b)

        print("Hello" + 10)   # TypeError

    except ZeroDivisionError as e:
        print("Error:", e)

    except ValueError as e:
        print("Error:", e)

except TypeError as e:
    print("Outer Error:", e)

print("Program End!")

print("Start Program")

try:
    a = int(input("Enter A Number: "))
    b = int(input("Enter B Number: "))
    print("Division:", a / b)
except ZeroDivisionError as e:
    print("Error:", e)
print("Program End!")

#we can only one Exception for every type of exception
try:
    doubtful code
except:
    alternate code
else:
    code excute if there is error
finally:
    it will execute always


"""


print("start Program")
try:
    a=int(input("Enter A Number: "))
    b=int(input("Enter B Number: "))
    print("Division :",a/b)
except Exception as e:
    print("Error:",e)
else:
    print("Division Complete!")
finally:
    print("program Finished!")
print("Program End!")
          

          

    
