"""
Dictionary:- Dictionary is collection of key:value pair(item).
Dictionary can hold Duplicate value but it can not hold duplicate key.
s={1:2345,2:6789,5:3423,'A':5634,'Aman':6789}
print(s)
print(type(s))

d={1:2345,2:6789,5:3423,'A':5634,'Aman':6789}
print(d)
print(d[5])
output:{1:2345,2:6655,5:3423}
#dictionary will update key with latest value

student={'sid':101,'sname':'Rahul Kumar','sclass':'XII'}

#Dictionary do not work with index=>it works with key
#Dictionary can not be sliced
#Dictionary can not be Replicate(Repeatition)
#But Dictionary can be Traverse
d={1:244,2:455,3:456,4:545,5:463}
for x in d:     #by default it itterates keys
    print(x)
   # OUTPUT:    1
2
3
4
5
d={1:244,2:455,3:456,4:545,5:463}
for x in d:
    print(d[x])
Output:
244
455
456
545
463

#Dictionary's Methods
keys,values,items

d={1:244,2:455,3:456,4:545,5:463}
for x in d.keys():  #itterative keys
    print(x)

d={1:244,2:455,3:456,4:545,5:463}
for x in d.values():  #itterative values
    print(x)

d={1:244,2:455,3:456,4:545,5:463}
for x in d.items():  #itterative items(pair)
    print(x)

d={1:244,2:455,3:456,4:545,5:463}
for key,value in d.items():  #itterative values
    print(key,value)

update,pop,popitem,clear,setdefault

d = {1:244,2:455,3:456,4:545,5:463}
print(d)
d.update({6:99})
print(d)

d = {1:244,2:455,3:456,4:545,5:463}

d2={7:88,8:77,4:22}
d.update(d2)
print(d)
d.pop(4)    #remove key 4's pair
print(d)
d.popitem() #remove last item
print(d)
d.setdefault(9,1100)    #it will add key 9 and value 1100
print(d)
d.setdefault(7,777)     #7 already exist,saved without any change
print(d)

copy,deepcopy:-
d1 = {1:244,2:455,3:456,4:545,5:463}
d2=d1
d2[3]=555
print(d1)
#it will not copy it will only assign a new name

d1 = {1:244,2:455,3:456,4:545,5:463}
d2=d1.copy()
d2[3]=555
print(d1)
print(d2)
#it will copy the dictionary and you will see changes in d2 only

d1 = {1:244, 2:455, 3:456, 4:545, 5:463}
d2 = d1.copy()
d2[2] = 999
d2['info'] = {}
d2['info']['name'] = 'Yogesh'
print(d1)
print(d2)
#copy is a shallow copy
#it will copy only outer object not inner.


"""

import copy
d1 = {1:244,2:455,'info':{'name':'Ravi','address':'Noida'},4:545,5:463}
d2=copy.deepcopy(d1)
d2[2]=999
d2['info']['name']='Yogesh'
print(d1)
print(d2)
#deepcopy will copy entire object
































