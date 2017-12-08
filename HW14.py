#Homework 14
#Programmer Paul Brodine
#Date of last revision Feb 04, 2016
#Purpose  Have user enter list of names / print names in reverse order

name_1=input("Type in a list of names, separated by a space with no comma: ")   #Requests input from user

list_1=name_1.title().split()               #Capitalizes names and turns into list
list_1.reverse()                            #Reverses the list

print(list_1)                               #Prints the list







    
