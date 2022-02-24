import turtle
t = turtle.Turtle()                     #1st look
t.speed(0)
turtle.bgcolor ("black")
def flower():
    for i in range (180):
        t.pencolor("white")
        t.circle (190-i, 90)
        t.left (90)
        t.circle(190-i, 90)
        t.left (18)
flower()

turtle.exitonclick()         


"""
import turtle
t = turtle.Turtle()                     #2nd look
t.speed(0)
def flower():
    for i in range (300):
        t.circle (190-i, 90)
        t.left (90)
        t.circle(190-i, 90)
        t.left (18)
flower()
mainloop()
turtle.exitonclick()    
"""