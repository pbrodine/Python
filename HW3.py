#Homework 3
#Programmer Paul Brodine
#Date of last revision Jan 19, 2016
#Purpose Make a program that allows user to input 4 numbers to be added.

a=float(input("Enter an integer: "))  #Allows user to input first integer
b=float(input("Enter another integer: "))  #Allows user to input second integer
c=float(input("Another integer please: "))  #Allows user to input third integer
d=float(input("This is the last integer, I promise: "))  #Allows user to input fourth integer

print("%11.2f"%a)  #Outputs the first number with 11 spaces and 2 decimal places.
print("%11.2f"%b)  #Outputs the second number with 11 spaces and 2 decimal places.
print("%11.2f"%c)  #Outputs the third number with 11 spaces and 2 decimal places.
print("+","%9.2f"%d)  #Outputs a "+" sign followed by 10 spaces and 2 decimal places.
print("__________")  #Outputs a row of underscores(=)
print("%11.2f"%(a+b+c+d))  #Outputs the sum of the four numbers with 11 spaces and 2 decimal places.

