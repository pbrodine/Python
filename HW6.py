#Homework 6
#Programmer Paul Brodine
#Date of last revision Jan 28, 2016
#Purpose Have user input an integer between 1 and 9999 / Output the number in words

x=int(input("Enter an integer between 1 and 9999:"))        #Prompts user for input

singles=['','one','two','three','four','five','six','seven','eight','nine','ten']       
teens=['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
tens=['','ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']       #Programs variables and lists

if x <=10:
    print(singles[x])       #Outputs variable for value less than / equal to 10

if x <=20 and x>10:
    print(teens[x-10])      #Outputs variable for value from 11 to 20

if x <100 and x >20:
    print(tens[x//10],singles[x%10])        #Outputs variable list for value from 21 to 99

if x <1000 and x >=100:
    print(singles[x//100],'hundred',tens[(x%100//10)],singles[x%10])        #Outputs variable list for value from 100 to 999

if x <1100 and x >=1000:
    print(singles[x//1000],'thousand',tens[(x%100//10)],singles[x%10])      #Outputs variable list for value from 1000 to 1099

if x <10000 and x >=1100:
    print(singles[x//1000],'thousand',singles[x%1000//100],'hundred',tens[(x%100//10)],singles[x%10])     #Outputs variable list for value from 1100 to 9999

if x >=10000 or x <=0:
    print("You failed to follow instructions. Good-Bye!")       #Outputs a negative for values 10000+ and 0 or less

