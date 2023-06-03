#NAME : KAVYA SRI GARIKIPATI
#NET ID: kxg3373
#STUDENT ID: 1001953373
#macOS Monterey version 12.5.1
#Writing the program in PYTHON Language and executing in CMD with the help of OMEGA SERVER
#The execution steps in CMD
#compiling and execution - [kxg3373@omega ~]$ python kxg3373_lab01.py

import os #importing os

def getDirectorySize(path):#adding the file sizes
    sum = 0
    list_of_files = os.listdir(path)#this allows to return a list which has the names of the entries in the directory which is given by path
    add_Slash = '/' #add slash
    for m in list_of_files: #using for loop to iterate list of entries
        full_path = path + add_Slash + m # calculate the full path
        if os.path.isfile(full_path):#checking if the path is an existing regular file or not
            sum += os.path.getsize(full_path) #Getting the file size
        elif os.path.isdir(full_path):# checking the specified path is an existing directory or not
            sum += getDirectorySize(full_path)
        else:
            print("end") # printing end
    return sum
path = os.getcwd() #getting current working directory",& "printing the working directory".
sum = getDirectorySize(path)# compute the folder size
print(sum)# sum is getting printed






































