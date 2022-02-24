import turtle                            #pentagon
t = turtle.Turtle ()
t.pensize(5)
t.speed(5)
t.color("orange", "red")
t.begin_fill()
t.forward (100)
t.right(72)
t.forward (100)
t.right(72)
t.forward (100)
t.right(72)
t.forward (100)
t.right(72)
t.forward (100)
t.right(72)
t.end_fill()
turtle.exitonclick()    


import turtle                           #octagon

design = turtle.Turtle()
design.color ("#F7024C", "pink")
design.begin_fill()
design.pensize(5)
for i in range(8):
   design.forward(60)
   design.left (45)


design.penup()
design.forward(150)
design.pendown()


for i in range (8):
   design.forward(60)
   design.left (45)

design.end_fill()
turtle.exitonclick()
turtle.done()
