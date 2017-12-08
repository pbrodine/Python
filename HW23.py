#Homework 23
#Programmer Paul Brodine
#Date of last revision Mar 23, 2016
#Purpose  Make an etch-a-sketch using arrow keys

import turtle
wn=turtle.Screen()      #Open turtle screen
crush=turtle.Turtle()   #Assign name to turtle
wn.title("Use Arrow Keys to Move. Press Spacebar to clear drawing") #Name title

#Turtle Definitions
def crush_up():
    crush.setheading(90)
    crush.forward(10)
    return

def crush_down():
    crush.setheading(270)
    crush.forward(10)
    return

def crush_left():
    crush.setheading(180)
    crush.forward(10)
    return

def crush_right():
    crush.setheading(0)
    crush.forward(10)
    return

def crush_clear():
    crush.clear()
    return

#Main Program (assigns keys)
wn.onkey(crush_up,'Up')
wn.onkey(crush_down,'Down')
wn.onkey(crush_left,'Left')
wn.onkey(crush_right,'Right')
wn.onkey(crush_clear,'space')
wn.listen()
wn.mainloop()
