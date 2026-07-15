"""
File HAndling
Types of  file
1)Binary File(.bin , .dat etc)
2)Text File(.docx, .xlsx, .pdf, .csv etc)

Text File
file_handler=open('file_name.extension','mode')
mode:- r,w,a,r+,w+,a+
file_handler.close()   #very important

| Mode | Description                                                          | File Must Exist? | Cursor Position |
| ---- | -------------------------------------------------------------------- | ---------------- | --------------- |
| `r`  | Read only                                                            | ✅ Yes            | Beginning       |
| `w`  | Write only (creates file if not exists, overwrites existing content) | ❌ No             | Beginning       |
| `a`  | Append (adds data at the end, creates file if not exists)            | ❌ No             | End             |
| `r+` | Read and Write                                                       | ✅ Yes            | Beginning       |
| `w+` | Read and Write (overwrites file, creates if not exists)              | ❌ No             | Beginning       |
| `a+` | Read and Append (creates file if not exists)                         | ❌ No             | End             |

Example:-
#'w' mode will open a file to write ifexist
#if file does not exist then it will a that file and open it


file = open('student.txt','w')
file.close()

#'w'mode will open a file to write if exist
#if file does not exist then it will create a that file and open it
file=open('student.txt','w')
file.close()

#'w' mode will erase old data and write the new one
file=open('student.txt','w')
file.write('Raman Singh')
file.close()

#'a' mode will add new data after the old data
file=open('student.txt','a')
file.write('\nSimran Khurana')
file.close()

#'write' method can write a string into the file
file=open('student.txt','a')
file.write('\n2635467')
file.close()

#'writelines' method to write multiple data
file=open('student.txt','a')
li=['\nAnu','\nManu','\nSohan','\nRohan']
file.writelines(li)
file.close()

file = open('student.txt','r')
data=file.read()    #it will read all data from a file
print(data)
file.close()

file=open('student.txt','r')
data=file.read(10)  #it will 10 character
print(data)
file.close()


file=open('student.txt','r')
data=file.readline()    #it will read first line only
print(data)
data=file.readline()    #it will read second line only
print(data)
file.close()

file=open('student.txt','r')
for i in range(10): #it will 10 lines
    data=file.readline()    
    print(data)
file.close()

#it will print all lines until it find blank/null lines
file=open('students.txt','r')
while True:
    data=file.readline()
    if len(data)==0:
        break
    print(data)
file.close()

file=open('student.txt','r')
data=file.readlines()    #it will read all lines
print(data)
file.close()

#itterate all lines one by one
file=open('student.txt','r')
data=file.readlines()#it will read first line only
for line in data:
    print(line)
file.close()


"""
file=open('student.txt','r')
print(file.tell())  #print Location of cursor in the file
file.close()

file=open('students.txt','r')
print(file.tell())  #print location of cursor in the file
print(file.read(10))
print(file.tell())
file.close()

file=open('students.txt','r')
print(file.tell())  #print location of cursor in the file
print(file.read(10))
file.seek(10)   #it will take cursor ot the 10th position from 0
print(file.tell())
file.close()


























