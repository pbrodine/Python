#Homework 4
#Programmer Paul Brodine
#Date of last revision Jan 19, 2016
#Purpose Have user input a word and replace all "a" with "*"

data=input("Type in a word:")  #Prompts user for an input / saves input as "data" variable

to_replace="a"  #tells program to replace all characters "a"

replacer="*"  #tells program to replace replaced characters with "*"

print(data.replace(to_replace,replacer))  #Outputs user's inputted data and replaces marked characters

