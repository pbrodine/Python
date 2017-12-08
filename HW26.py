#Homework 26
#Programmer Paul Brodine
#Date of last revision Feb 29, 2016
#Purpose  Draw a smiley face

import turtle
wn=turtle.Screen()
crush=turtle.Turtle()

#Main Program
crush.hideturtle()
crush.speed(10)

#Face
crush.penup()
crush.goto(0,-200)
crush.width(5)
crush.pendown()
crush.fillcolor('yellow')
crush.begin_fill()
crush.circle(225)
crush.end_fill()

#Eyes
crush.penup()
##Right eye
crush.goto(67,77)
crush.pendown()
crush.fillcolor('white')
crush.begin_fill()
crush.circle(35)
crush.penup()
##Left eye
crush.goto(-67,77)
crush.pendown()
crush.circle(35)
crush.end_fill()
##Left pupil
crush.fillcolor('blue')
crush.begin_fill()
crush.circle(12)
crush.penup()
##Right pupil
crush.goto(67,77)
crush.pendown()
crush.circle(12)
crush.end_fill()
crush.penup()

#Mouth
crush.goto(-100,-40)
crush.setheading(270)
crush.pendown()
crush.fillcolor('black')
crush.begin_fill()
crush.circle(100,180)
crush.goto(-100,-40)
crush.end_fill()
crush.penup()

#Nose
crush.goto(0,60)
crush.setheading(180)
crush.pendown()
crush.circle(30,180,2)
wn.mainloop()











