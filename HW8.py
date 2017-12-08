#Homework 9
#Programmer Paul Brodine
#Date of last revision Jan 22, 2016
#Purpose Have user input 3 integers / If ANY Positive integers = Yes / No

var1=int(input("Enter an integer:"))    #Prompts user to enter an integer
var2=int(input("Enter an integer:"))    #"                              "
var3=int(input("Enter an integer:"))    #"                              "

if (var1 >0) or (var2 >0) or (var3 >0): 
    print("Nailed it!")                 #Tells program to output affirmative if any of the variables are positive

else:
    print("Not this time:(")            #Tells program to output negative if none of the variables are positive

