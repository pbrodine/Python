#Homework 5
#Programmer Paul Brodine
#Date of last revision Jan 19, 2016
#Purpose Have user input a word and replace all "a" and "A" with "*"

data=input("Type in a word:")  #Prompts user for an input / saves input as "data" variable

to_replace=("A")  #tells program to replace all characters "A"

replacer=("a")  #tells program to replace replaced characters with "a"

new_data=(data.replace(to_replace,replacer))  #Assigns new variable with all "A" replaced as "a"

to_replace=("a")  #tells program to replace all characters "a"

replacer=("*")  #tells program to replace replaced characters with "*"

print(new_data.replace(to_replace,replacer))  #Outputs user's inputted data and replaces marked characters

