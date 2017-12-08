#Homework 25
#Programmer Paul Brodine
#Date of last revision Apr 4, 2016
#Purpose  Implement a paint program using python. Should be able to choose a few colors and pen size.

#Prep Turtle
import turtle
wn=turtle.Screen()
crush=turtle.Turtle()
crush.speed(0)
crush.penup()
crush.turtlesize(2)
wn.title("Drag the circle to draw.")


#Define Menu Area
crush.goto(-350,-215)
crush.pendown()
crush.goto(350,-215)

#Color-Black
crush.penup()
crush.goto(-270,-240)
crush.shape('square')
crush.stamp()

#Color-Green
crush.goto(-225,-240)
crush.color('green')
crush.stamp()

#Color-Blue
crush.goto(-180,-240)
crush.color('blue')
crush.stamp()

#Color-Yellow
crush.goto(-135,-240)
crush.color('yellow')
crush.stamp()

#Size-XL
crush.goto(270,-240)
crush.shape('circle')
crush.color('black')
crush.stamp()

#Size-L
crush.goto(225,-240)
crush.turtlesize(1.5)
crush.stamp()

#Size-R
crush.goto(180,-240)
crush.turtlesize(1)
crush.stamp()

#Size-S
crush.goto(135,-240)
crush.turtlesize(.5)
crush.stamp()
crush.speed(5)
crush.goto(0,0)


#Selector
def h1(x,y):
    if y>-260 and y<-220:
        if x>-290 and x<-250:
            crush.color('black')
            crush.pencolor('black')

        elif x>-245 and x<-205:
            crush.color('green')
            crush.pencolor('green')

        elif x>-200 and x<-160:
            crush.color('blue')
            crush.pencolor('blue')
        
        elif x>-155 and x<-115:
            crush.color('yellow')
            crush.pencolor('yellow')

        elif x>110 and x<150:
            crush.turtlesize(.5)
            crush.pensize(1)

        elif x>155 and x<195:
            crush.turtlesize(1)
            crush.pensize(2)

        elif x>200 and x<240:
            crush.turtlesize(1.5)
            crush.pensize(4)

        elif x>245 and x<290:
            crush.turtlesize(2)
            crush.pensize(8)

    else:
        crush.penup()
        crush.goto(x,y)

#Drag
def h2(x,y):
    crush.pendown()
    crush.goto(x,y)

#Program
crush.ondrag(h2)
wn.onclick(h1)

wn.mainloop()








        


