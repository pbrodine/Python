#Homework 20
#Programmer Paul Brodine
#Date of last revision Mar 21, 2016
#Purpose  Ask user to input an encrypted message (Upper-Case Letters, no spaces) and then input keyword for decryption

#####Variables
text_list=[]    #Create an empty list
key_list=[]     #Create an empty list

encryption=input("Enter a sequence of upper-case letters (no spaces or punctuation): ")  #Request input from user

text_length=len(encryption)  #Determines length of user input

keyword=input("Enter a keyword using upper-case letters (no spaces or punctuation): ")  #Request input from user

badkey=keyword*text_length  #Assigns variable (repeats user input times the length of the user input)

key=badkey[0:text_length]   #Assigns variable (takes previous variable and matches length to first user input)
#####Program

for x in encryption:
    text_list.append(ord(x))    #adds the ASCII number for each user input letter to a list

for x in key:
    key_list.append(ord(x))     #adds the ASCII number for each user input letter to a list
    
for x in text_list:
    message=chr((x-key_list[0])%26+65)   #Assigns variable(Subtracts first number in second list from x in first list. Divides to get remainder and adds 65. Changes from ASCII to character)
    key_list.pop(0)     #Removes the first item in list
    print(message, end='')       #prints the translated cipher without moving to new line
    

    


