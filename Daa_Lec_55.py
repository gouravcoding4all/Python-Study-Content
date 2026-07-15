"""
Collection
Sequnce Data Type
    List,Tuple

List_name=[val1,val2,val3,...] #list
Tuple_name=(value1,val2,val3,...) #Tuple

List:-List is a collection of hetregenous(different) data type elements

Ways to create a list
li=[2,43,455,678,89,34]
li=[34,'Aman',35,67,True,32+8j]
li=[]
li=list([2,43,455,678,89,34])
li=list((23,45,56,78))
li=list()
print(li)
print(type(li))

Index:-
forward index(0,1,2,3,...)
backward index(-1,-2,-3,...)
list_name[index]

li=[2,3,4,5,6]
print(li[2])
print(li[-4])

#List also supports Replication
if u will multiply a collection with a number it will repeat that list for number times

li=[1,2,0,3,4,5]
print(li*3)         #repeat 3 times

li=[23,54,56,89,41]
print(li)   #repeat 3 times
for x in li:
    print(x)

built in functions
sum,max,min,len

li=[21,78,65,12,57,798,35]
print(li)
print(sum(li))
print(max(li))
print(min(li))
print(len(li))
print(sum(li)/len(li))

list's methods
append,extend,insert

li=[23,54,6,789,54]
print(li)
li.append(99)
print(li)
li.insert(2,88)
print(li)
li2=[11,22,33]
li.extend(li2)
print(li)

pop,remove,clear,del(keyword)

li=[23,54,6,789,54,99]
print(li)
li.pop()    #pop will remove last elements
print(li)
li.pop(1)   #pop(index)
print(li)
li.remove(6)    #remove(value)
print(li)
del li[1]
print(li)
li.clear()
print(li)

li=[56,43,86,23,89,12]
print(li)
li.reverse()
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)

index,count


"""
li=[53,56,43,78,43,43,56,34,67,34]
print(li)
print(li.count(43))
print(li.index(56))
print(li.index(56,2))
