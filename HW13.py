#Homework 13
#Programmer Paul Brodine
#Date of last revision Feb 02, 2016
#Purpose  Have user enter two lists of names / print names common to both lists

name_1=input("Type in a list of names, separated by a space with no commas: ")       #Asks for user input
name_2=input("Type in a list of names, separated by a space with no commas: ")       #Asks for user input

list_1=name_1.title().split()                   #Titles and lists the input
list_2=name_2.title().split()                   #Titles and lists the input

common=False                                    #Sets default common to False

for x in list_1:
    if x in list_2:
        common=True                             #Sets common to true if there is a common name between both lists

if common:
    print("The common name is",set(list_1)&set(list_2)) #Outputs the common name
else:
    print("No names in common.")                        #Outputs no name in common





    
