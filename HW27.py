#Homework 27
#Programmer Paul Brodine
#Date of last revision Apr 10, 2016
#Purpose  Create a stop-light. Press Spacebar to cycle through the colors.

#Setup
import turtle
wn=turtle.Screen()
crush=turtle.Turtle()
crush.speed(0)
wn.title('Press Spacebar to cycle through lights')

#Frame
crush.penup()
crush.goto(-130,-250)
crush.width(5)
turtle.pencolor('black')
crush.fillcolor('yellow')
crush.begin_fill()
crush.pendown()
crush.goto(130,-250)
crush.left(90)
crush.goto(130,250)
crush.left(90)
crush.goto(-130,250)
crush.left(90)
crush.goto(-130,-250)
crush.end_fill()

#Red Light
crush.left(90) 
crush.penup() 
crush.goto(0,85)
crush.fillcolor('black')
crush.begin_fill() 
crush.pendown()  
crush.circle(80) 
crush.end_fill()

#Yellow Light
crush.penup()
crush.goto(0,-80)
crush.fillcolor('black')
crush.begin_fill()
crush.pendown()
crush.circle(80)
crush.end_fill()

#Green Light
crush.penup()
crush.goto(0,-245)
crush.fillcolor('black')
crush.begin_fill()
crush.pendown()
crush.circle(80)
crush.end_fill()
crush.penup()

#Light Control
crush.turtlesize(7.8)
crush.color('green')
crush.shape('circle')
crush.goto(0,-165)

def change():
    if crush.ycor()==-165:
        crush.color('yellow')
        crush.goto(0,0)
    elif crush.ycor()==0:
        crush.color('red')
        crush.goto(0,165)  
    elif crush.ycor()==165:
        crush.color('green')
        crush.goto(0,-165)
        return

wn.onkey(change,'space')
wn.listen()

wn.mainloop()













