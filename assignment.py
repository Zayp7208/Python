"""
CTI 110
p_TURTLE - Turtle graphics
Xazieron Puryear
"""
#set up thr turtle
import turtle

t = turtle.Turtle() 

t.pensize(3)
t.pencolor("blue")

##t.left(90)
##t.forward(100)
##t.right(180)
##t.forward(100)

t.pencolor('green')
t.pendown
t.goto(0, 0)
t.goto(-50, -100)
##t.goto(-100, 100)

t.penup
t.goto(0,0)
t.goto(-50, 100)
t.goto(0,0)
t.goto(50,100)
t.goto(0,0)

t.pendown
t.goto(50,-100)

t.penup()
t.goto(200,-100)
t.pendown()
