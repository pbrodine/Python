#Homework 22
#Programmer Paul Brodine
#Date of last revision Apr 10, 2016
#Purpose  Ask user for lower-case input, output braille representation of letter

#Dictionaries for top, middle, and bottom lines of braille
top={'a':'* ','b':'* ','c':'**','d':'**','e':'* ','f':'**','g':'**','h':'* ','i':' *','j':' *','k':'* ','l':'* ','m':'**','n':'**','o':'* ','p':'**','q':'**','r':'* ','s':' *','t':' *','u':'* ','v':'* ','w':' *','x':'**','y':'**','z':'* '}

middle={'a':'  ','b':'* ','c':'  ','d':' *','e':' *','f':'* ','g':'**','h':'**','i':'* ','j':'**','k':'  ','l':'* ','m':'  ','n':' *','o':' *','p':'* ','q':'**','r':'**','s':'* ','t':'**','u':'  ','v':'* ','w':'**','x':'  ','y':' *','z':' *'}

bottom={'a':'  ','b':'  ','c':'  ','d':'  ','e':'  ','f':'  ','g':'  ','h':'  ','i':'  ','j':'  ','k':'* ','l':'* ','m':'* ','n':'* ','o':'* ','p':'* ','q':'* ','r':'* ','s':'* ','t':'* ','u':'**','v':'**','w':' *','x':'**','y':'**','z':'**'}

#prompts user for string
letters=input('Enter up to 15 lower-case letters: ')
letter_list=[]  #empty list to append later

for chr in letters: 
    clean=chr.rstrip()
    letter_list.append(clean)   #appends clean line of input to list

for letter in letter_list:
    clean=letter.rstrip()
    print(top[letter],end='')   #prints top line of braille for letters in input

print()

for letter in letter_list:
    clean=letter.rstrip()
    print(middle[letter],end='')    #prints middle line of braille for letters in input

print()

for letter in letter_list:
    clean=letter.rstrip()
    print(bottom[letter],end='')    #prints bottom line of braille for letters in input














