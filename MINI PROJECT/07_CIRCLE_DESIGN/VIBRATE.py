import turtle

t= turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
t.pencolor("white")

x=0
y=0

t.penup()
t.goto(0,200)
t.pendown()

while True:
    t.forward (x)
    t.right (y)
    x= x+3
    y= y+1
    if y== 200:
        break
    t.hideturtle()

turtle.done()
turtle.exitonclick()    