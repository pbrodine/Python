#Homework 19
#Programmer Paul Brodine
#Date of last revision Mar 21, 2016
#Purpose  Ask user to input a message (Upper-Case Letters, no spaces) and then input keyword for encryption

#####Variables
text_list=[]    #Create an empty list
key_list=[]     #Create an empty list

plaintext=input("Enter a sequence of upper-case letters (no spaces or punctuation): ")  #Request input from user

text_length=len(plaintext)  #Determines length of user input

keyword=input("Enter a keyword using upper-case letters (no spaces or punctuation): ")  #Request input from user

badkey=keyword*text_length  #Assigns variable (repeats user input times the length of the user input)

key=badkey[0:text_length]   #Assigns variable (takes previous variable and matches length to first user input)
#####Program

for x in plaintext:
    text_list.append(ord(x))    #adds the ASCII number for each user input letter to a list

for x in key:
    key_list.append(ord(x))     #adds the ASCII number for each user input letter to a list
    
for x in text_list:
    cipher=chr((x+key_list[0])%26+65)   #Assigns variable (adds x in list and first number in other list. Divides to get remainder and adds 65. Changes from ASCII to character)
    key_list.pop(0)     #Removes the first item in list
    print(cipher, end='')       #prints the translated cipher without moving to new line
    

    


