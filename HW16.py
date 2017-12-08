#Homework 16
#Programmer Paul Brodine
#Date of last revision Feb 22, 2016
#Purpose  Read a list of integers from file trash.dat / Print integers in ascending order

infile=open('trash.dat','r')            #Opens trash.dat file

file_contents=infile.readlines()        #Assigns variable for file contents

infile.close()                          #Closes file

integer_list=[]                         #Starts an empty list

for x in file_contents:                 #For each 'x' in file:
    numb=int(x)                         #Assign variable and turn each 'x' into integer
    integer_list.append(numb)           #Add variable to list

integer_list.sort()                     #Sorts list

for x in integer_list:                  #For each 'x' in file:
    print(x)                            #Prints each 'x'
    
