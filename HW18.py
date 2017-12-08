#Homework 18
#Programmer Paul Brodine
#Date of last revision Feb 29, 2016
#Purpose  Ask user for lower-case input, output braille representation of letter

braille={'a':"""* 

  """,'b':"""*
*
  """,'c':"""**

  """,'d':"""**
 *
  """,'e':"""*
 *
  """,'f':"""**
*
  """,'g':"""**
**
  """,'h':"""*
**
  """,'i':""" *
*
  """,'j':""" *
**
  """,'k':"""*

* """,'l':"""*
*
* """,'m':"""**

* """,'n':"""**
 *
* """,'o':"""*
 *
* """,'p':"""**
*
* """,'q':"""**
**
* """,'r':"""*
**
* """,'s':""" *
*
* """,'t':""" *
**
* """,'u':"""*

**""",'v':"""*
*
**""",'w':""" *
**
 *""",'x':"""**

**""",'y':"""**
 *
**""",'z':"""*
 *
**"""}                                          #Programs a braille dictionary for each lower-case letter


letter=input("Enter a lower-case letter: ")     #Assigns variable and requests input

print(braille[letter])                          #Prints the user-input braille letter


         
