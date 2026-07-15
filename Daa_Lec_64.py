"""
In Python, pickle is a built-in module used for serializing and deserializing
Python object structure.


Store Management System
Customer(cid,cname ,cadd,amob)
product(pid,pname,price,pdesc)
orders(cid,pid,qty)

1-Add Customer
2-View All Customer
3-Delete A Customer
4-Add Product
5-View All Products
6-Update PRoduct's Price
7-Place An Order
8-View All Orders
9-View Orders By CID
0-Exit


"""

#Importing Required Libraries
import pickle

#A Method To Get Customer Information
def getCustomer():
    file=open('customer.bin','rb')
    cus=dict()
    try:
        while True:
            cus.update(pickle.load(file))
    except:
        pass
    file.close()
    return cus

#A Method To Update Customer Information
def updateCustomer(cus):
    file=open('customer.bin','wb')
    for cid,info in cus.items():
        pickle.dump({cid:info},file)
    file.close()

#A Method to add customer information:-
    def addCustomer():
        cid=input("\n\tEnter NEw Customer Id:")
        cus=getCustomer()
        if cus.get(cid,False):
            print("\n\tCustomer Already Exist on this ID!")
        else:
            cname=input("\tEnter Customer Name: ")
            cadd=input("\tEnter Customer Address: ")
            cmob=input("\tEnter Customer Mobile: ")
            cus.update({cid:[cname,cadd,cmob]})
            updateCustomer(cus)
            print("\n\tCustomer Added Successfully!")
    
#A method to view All Customer's Information
def viewCustomers():
    cus=getCustomer()
    for cid,info in cus.items():
        print("\n\tCustomer ID :",cid )
        print("\tCustomer Name :",info[0])
        print("\tCustomer Address :",info[1])
        print("\tCustomer Mobile :",info[2])
        print("\t---------------------------")

#Dashboard
while True:
    print("\n\tStore Management System")
    print('''
        1-Add Customer
        2-View All Customer
        3-Delete A Customer
        4-Add product
        5-View All Products
        6-Update Product's Price
        7-Place An Orders
        8-View All Orders
        9-view Orders By CID
        0-Exit
        ''')
    ch=int(input("\tEnter your Choice : "))
    if ch==0:
        print("\n\tBye-Bye Admin!")
        break
    elif ch==1:
        addCustomer()
        input("\tPress Enter to Continue..")
    elif ch==2:
        viewCustomers()
        input("\tPress Enter To Continue..")
        
        










    
