#Homework 21
#Programmer Paul Brodine
#Date of last revision Feb 29, 2016
#Purpose  Menu program / allow user to read, save, add, delete, change, show sorted lists from file stuff.txt

#Menu List
print('1 to read file.')
print('2 to add a record.')
print('3 to delete a record.')
print('4 to change a record.')
print('5 to sort file by ID Number.')
print('0 to end program.')
print('\n')
numb=int(input('Enter a selection from above: '))   #Requests Input

while numb >0 and numb <6:      #Runs Main Program until another key is pressed
    if numb == 1:               #Executes if 1 is selected
        infile=open('stuff.txt','r')    
        file_contents=infile.readlines()
        infile.close()
        for line in file_contents:
            clean_line=line.rstrip()
            print(clean_line)

    if numb == 2:               #Executes if 2 is selected
        record=input('Enter the record you would like to add: ')

        outfile=open('stuff.txt','a')
        outfile.write('\n'+record)
        outfile.close()

    if numb == 3:               #Executes if 3 is selected
        ID=input('Enter the ID number to be removed: ')

        outfile=open('stuff.txt','r')
        file_contents=outfile.readlines()
        outfile.close()

        outfile=open('stuff.txt','w')
        for line in file_contents:
            if ID not in line:
                outfile.write(line)
        outfile.close()
                
    if numb == 4:               #Executes is 4 is selected
        ID=input('Enter the ID number of the record you would like to change: ')
        old=input('Enter the information to be changed exactly as it appears: ')
        new=input('Enter the new information: ')

        outfile=open('stuff.txt','r')
        file_contents=outfile.readlines()
        outfile.close()
        for line in file_contents:
            if ID in line:
                change=line.replace(old,new)

        outfile=open('stuff.txt','w')
        for line in file_contents:
            if ID not in line:
                outfile.write(line)
        outfile.close()

        outfile=open('stuff.txt','a')
        outfile.write(change)
        outfile.close()
        
    if numb == 5:               #Executes if 5 is selected
        file_list=[]

        outfile=open('stuff.txt','r')
        file_contents=outfile.readlines()
        outfile.close()
        for line in file_contents:
            file_list.append(line)
        file_list.sort()

        outfile=open('stuff.txt','w')
        for line in file_list:
            outfile.write(line)
        outfile.close()
            
    #Runs the menu list
    print('\n')
    print('1 to read file.')
    print('2 to add a record.')
    print('3 to delete a record.')
    print('4 to change a record.')
    print('5 to sort file by ID Number.')
    print('0 to end program.')
    print('\n')
    numb=int(input('Enter a selection from above: '))
    
    










    
















    


