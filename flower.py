import turtle

flower = turtle.Turtle()
flower.color ("#FF0000", "yellow")
flower.begin_fill()
for i in range (52):
  flower.forward (100)
  flower.left(170)
flower.end_fill()

flower.penup()
flower.forward(200)
flower.pendown()

flower.begin_fill()
for i in range (52):
  flower.forward (200)
  flower.left(170)
flower.end_fill()

flower.penup()
flower.forward(400)
flower.pendown()

flower.begin_fill()
for i in range (52):
  flower.forward (70)
  flower.left(170)
flower.end_fill()
turtle.done()
