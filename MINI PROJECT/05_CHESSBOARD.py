import turtle
pen= turtle.Turtle()

def square(size):
    for i in range(4):
        pen.forward(size)
        pen.left(90)
pen.speed (0)
x=0
y=0
count = 2
while True:
     pen.goto(x,y)
     pen.down()
     x= x+20

     pen.begin_fill()
     if count %2 ==0:
         pen.fillcolor("black")
     else:
         pen.fillcolor ("white")

     count = count+1
     square(20)
     pen.end_fill()

     if x>= 20*8:
         x=0
         y= y+20
         pen.penup()
         count = count+1

     if y>= 20*8:
         break

pen.hideturtle()
turtle.done()

