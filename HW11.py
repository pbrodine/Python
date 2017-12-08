#Homework 11
#Programmer Paul Brodine
#Date of last revision Jan 22, 2016
#Purpose  Have user enter an integer / Countdown from input

var=int(input("Enter an integer:")) #Prompts user to enter an integer

while (var >0):     #Initiates a loop that stops when the number is greater than 0
    print('\n',var,'\n')  #Prints the variable number
    var=var-1       #Subtracts 1 from the variable
    
print("Blast Off!!!")               #Outputs when the countdown reaches 0
