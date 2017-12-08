#Homework 17
#Programmer Paul Brodine
#Date of last revision Feb 29, 2016
#Purpose  Build a dictionary from dicter.dat file containing two words per line separated
#by a comma. User inputs one word, program outputs second word.

infile=open('dicter.dat','r')                       #Opens a file and assigns variable

file_contents=infile.readlines()                    #Assigns variable to lines in file

infile.close()                                      #Closes a file

my_dict={}                                          #Assigns a variable for a dictionary    
choices=[]                                          #Assigns a variable for a list

for x in file_contents:                             #For all strings:
    clean_line=x.rstrip()                           #Cleans the line at beginning and end
    word=clean_line.split(',')                      #Removes any commas
    my_dict[word[0]]=word[1]                        #Adds word and definition to dictionary 
    choices.append(word[0])                         #Adds first word only to list

print("Read the list below.")                       #Print statement

print('\n')                                         #Print blank line

for x in choices:                                   #For all strings:
    print(x)                                        #Print all strings in list

print('\n')                                         #Print blank line

selection=input("Enter a word from the list: ")     #Assigns variable and prompts user for input
    
print(my_dict[selection])                           #Prints the second word based on what the user input




