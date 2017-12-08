#Homework 24
#Programmer Paul Brodine
#Date of last revision Apr 4, 2016
#Purpose  Create a scatterplot using data from a file "trash.dat"


#Prep Turtle
import turtle
wn=turtle.Screen()
crush=turtle.Turtle()
crush.hideturtle()
crush.speed(0)
crush.shape('circle')
crush.turtlesize(.3)

#X and Y Axis
def gohome():
    crush.penup()
    crush.goto(-300,-250)
    crush.setheading(0)
    
gohome()
crush.pendown()
crush.goto(-300,250)
gohome()
crush.pendown()
crush.goto(300,-250)
gohome()

#Read file
infile=open('trash.dat','r')
plot=infile.readlines()
infile.close

#Plot Points
for line in plot:
    clean_line=line.rstrip()
    x_y=clean_line.split(',')
    crush.forward(int(x_y[0]))
    crush.left(90)
    crush.forward(int(x_y[1]))
    crush.stamp()
    gohome()

wn.mainloop()

