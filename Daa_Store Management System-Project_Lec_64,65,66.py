"""
Store Management System
Customer (cid , cname , cadd , cmob)
Product  (pid , pname , price , pdesc)
orders   (cid , pid , qty)

1- Add Customer
2- View All Customer
3- Delete A Customer
4- Add Product
5- View All Products
6- Update Product's Price
7- Place An Order
8- View All Orders
9- View Orders By CID
0- Exit

"""

# IMPORTING REQUIRED LIBRARIES
import pickle

# A METHOD TO GET CUSTOMER INFORMATION
def getCustomer():
    file = open('customer.bin','rb')
    cus = dict()
    try:
        while True:
            cus.update( pickle.load(file) )
    except:
        pass
    file.close()
    return cus

# A METHOD TO GET PRODUCT INFORMATION
def getProduct():
    file = open('product.bin','rb')
    pro = dict()
    try:
        while True:
            pro.update( pickle.load(file) )
    except:
        pass
    file.close()
    return pro

# A METHOD TO UPDATE CUSTOMER INFORMATION
def updateCustomer(cus):
    file = open('customer.bin','wb')
    for cid,info in cus.items():
        pickle.dump({cid:info},file)
    file.close()

# A METHOD TO UPDATE PRODUCT INFORMATION
def updateProduct(pro):
    file = open('product.bin','wb')
    for pid,info in pro.items():
        pickle.dump({pid:info},file)
    file.close()

# A METHOD TO ADD CUSTOMER INFORMATION
def addCustomer():
    cid = input("\n\tEnter New Customer ID : ")
    cus = getCustomer()
    if cus.get(cid,False):
        print("\n\tCustomer Already Exist on This ID!")
    else: 
        cname = input("\tEnter Customer Name : ")
        cadd = input("\tEnter Customer Address : ")
        cmob = input("\tEnter Customer Mobile : ")
        cus.update({cid:[cname,cadd,cmob]})
        updateCustomer(cus)
        print("\n\tCustomer Added Successfully!")

# A METHOD TO VIEW ALL CUSTOMER's INFORMATION
def viewCustomers():
    cus = getCustomer()
    for cid,info in cus.items():
        print("\n\tCustomer ID :",cid)
        print("\tCustomer Name :",info[0])
        print("\tCustomer Address :",info[1])
        print("\tCustomer Mobile :",info[2])
        print("\t-------------------------------------")

# A METHOD TO DELETE A CUSTOMER
def deleteCustomer():
    cid = input("\n\tEnter Customer ID To Delete : ")
    cus = getCustomer()
    c = cus.get(cid,False)
    if c:
        print("\n\tCustomer Name :",c[0])
        print("\tCustomer Address :",c[1])
        print("\tCustomer Mobile :",c[2])
        choice = input("\n\tDo You Want To Delete(Y/n) : ")
        if choice in 'Yy':
            cus.pop(cid)
            updateCustomer(cus)
            print('\n\tCustomer Deleted Successfully!')
    else:
        print("\n\tCustomer Not Found on this ID!")

# A METHOD TO ADD PRODUCT INFORMATION
def addProduct():
    pid = input("\n\tEnter New Product ID : ")
    pro = getProduct()
    if pro.get(pid,False):
        print("\n\tProduct Already Exist!")
    else:
        pname = input("\tEnter Product Name : ")
        price = input("\tEnter Product Price : ")
        pdesc = input("\tAbout The Product : ")
        data = {pid:[pname,price,pdesc]}
        pro.update(data)
        updateProduct(pro)
        print("\n\tProduct Addedd Successfully!")

# A METHOD TO VIEW ALL PRODUCTS INFORMATION
def viewProducts():
    pro = getProduct()
    print("\n\tPID   P_NAME       PRICE   ABOUT PRODUCT")
    for pid,info in pro.items():
        print(f"\t{pid:<5} {info[0]:<12} {info[1]:<7} {info[2]}")

# A METHOD TO UPDATE PRODUCT's PRICE
def updateProductPrice():
    pid = input("\n\tEnter Product ID TO Update Price : ")
    pro = getProduct()
    p = pro.get(pid,False)
    if p:
        print("\n\tProduct Name :",p[0])
        print("\tProduct Old Price :",p[1])
        price = input("\n\tEnter New Price : ")
        data = {pid:[p[0],price,p[2]]}
        pro.update(data)
        updateProduct(pro)
        print("\tPrice Updated Successfully!")
    else:
        print("\n\tProduct Does Not Exist!")

# A METHOD TO PLACE AN ORDER
def placeAnOrder():
    cid = input("\n\tEnter Customer ID : ")
    cus = getCustomer().get(cid,False)
    if cus:
        print("\n\tCustomer Name :",cus[0])
        print("\tCustomer Address :",cus[1])
        pid = input("\n\tEnter Product ID : ")
        pro = getProduct().get(pid,False)
        if pro:
            print("\n\tProduct Name :",pro[0])
            print("\tProduct Price :",pro[1])
            qty = input("\tEnter Quantity : ")
            print("\n\tTotal Bill :",float(pro[1])*int(qty))
            file = open('orders.bin','ab')
            data = [cid,pid,qty]
            pickle.dump(data,file)
            file.close()
            print("\n\tOrder Placed Successfully!")
        else:
            print("\n\tProduct Not Found!")
    else:
        print("\n\tCustomer Not Found!")

# A METHOD TO VIEW ALL ORDERS
def viewAllOrders():
    file = open('orders.bin','rb')
    try:
        oid = 1000
        while True:
            oid = oid+1
            data = pickle.load(file)
            cus = getCustomer().get(data[0] , False)
            pro = getProduct().get(data[1] , False)
            qty = data[2]
            if cus and pro and qty:
                print("\nOrder ID :",oid)
                print("\tCustomer Name :",cus[0])
                print("\tCustomer Address :",cus[1])
                print("\tCustomer Mobile :",cus[2])
                print("\tProduct Name :",pro[0])
                print("\tProduct Price :",pro[1])
                print("\tAbout the Product :",pro[2])
                print("\tOrdered Quantity :",qty)
                print("\tTotal Bill :",float(pro[1])*int(qty))
    except:
        pass
    file.close()

# A METHOD TO VIEW ORDERS BY CID
def orderByCID():
    cid = input("\n\tEnter Customer ID To View Orders : ")
    if getCustomer().get(cid,False):
        file = open('orders.bin','rb')
        try:
            oid = 1000
            while True:
                oid = oid+1
                data = pickle.load(file)
                cus = getCustomer().get(data[0] , False)
                pro = getProduct().get(data[1] , False)
                qty = data[2]
                if cus and pro and qty and data[0]==cid:
                    print("\nOrder ID :",oid)
                    print("\tCustomer Name :",cus[0])
                    print("\tCustomer Address :",cus[1])
                    print("\tCustomer Mobile :",cus[2])
                    print("\tProduct Name :",pro[0])
                    print("\tProduct Price :",pro[1])
                    print("\tAbout the Product :",pro[2])
                    print("\tOrdered Quantity :",qty)
                    print("\tTotal Bill :",float(pro[1])*int(qty))
        except:
            pass
        file.close()        
    else:
        print("\n\tCustomer Not Found!")

# DASHBOARD 
while True:
    print("\n\tSTORE MANAGEMENT SYSTEM")
    print('''
        1- Add Customer
        2- View All Customer
        3- Delete A Customer
        4- Add Product
        5- View All Products
        6- Update Product's Price
        7- Place An Order
        8- View All Orders
        9- View Orders By CID
        0- Exit
    ''')
    ch = int(input("\tEnter Your Choice : "))
    if ch==0:
        print("\n\tBye-Bye Admin!")
        break
    elif ch==1:
        addCustomer()
    elif ch==2:
        viewCustomers()
    elif ch==3:
        deleteCustomer()
    elif ch==4:
        addProduct()
    elif ch==5:
        viewProducts()
    elif ch==6:
        updateProductPrice()
    elif ch==7:
        placeAnOrder()
    elif ch==8:
        viewAllOrders()
    elif ch==9:
        orderByCID()
    else:
        print("\n\tWrong Entered\n\tTry Again!")
    input("\tPress Enter To Continue..")







    
