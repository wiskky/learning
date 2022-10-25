#This program teachess you how to use file system in pythom
#While open file you have to close it
#There are 3 modes  in file 'r' to read, 'w' to write and 'a' to append and the default mode is 't' text mode
"""
1. f = open("test.py", "w")
/* perform file operations here
f.close()


2. #you can also use try and finally method. We have encoding for linux as "urf-8" and for window as "cp1252"
try:
  f = open("test.py","w",encoding="urf-8")
  #***perform file operations here***
finally:
  f.close()

  #3.***************ALWAYS USE THIS 3RD METHOD******************
with open("filedoc.py","w",encoding="cp1252") as f:
    f.write("My first line\n")
    f.write("My second line\n")
    f.write("My third line\n")
    #no need to close file in with statement

#4. To open a file to read from it**†**********""""""
with open("test1.py","r") as f:
    fopen = f.read()
    print(fopen)
    print(fopen[4])   #to print the 1st 4 letter
    print(f.tell())   #Get the currect file position
    print(f.seek(0))  #Bringing file cursor into initial position
    f.close()

#Note: you can use for loop with the file and readline() function
with open("test1.py","r") as f:
    for word in f:
        print(word, end=' ') #we use end with print in other to remove paragraph

"""
#To read line in the file in python*******""*"""""""
with open("filedoc.py","r") as f:
    print(f.readline())
    f.close()
