#Homework 7
#Programmer Paul Brodine
#Date of last revision Jan 22, 2016
#Purpose Have user input 3 integers / Increasing values = yes or no

var1=input("Enter an integer:") #Prompts user to enter an integer
var2=input("Enter an integer:") #"                              "
var3=input("Enter an integer:") #"                              "

if (var1<var2) and (var2<var3): 
    print("Yes!")               #Tells program to output affirmative if the variables are entered in increasing order

else:
    print("No way Jose...")     #Tells program to output negative if the variables are not entered in increasing order

