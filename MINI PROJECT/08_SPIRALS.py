import turtle                               
"""
#1st spiral
colors = ['pink', 'yellow', 'orange', 'green', 'purple', 'red']

turtle.bgcolor ("black")
t = turtle.Turtle()
t.speed(0)
for i in range(200):
    t.pencolor(colors[i%6])
    t.width(i/100)
    t.forward(i)
    t.left(60)
turtle.exitonclick()    


#2nd spiral

turtle.bgcolor("black")
t = turtle.Turtle()
t.width(2)
t.speed(0)

color = ('cyan', 'pink', 'white')
for i in range (150):
    t.pencolor(color[i%3])
    t.forward (i*4)
    t.right(120)

turtle.exitonclick()
"""


#3rd spiral

turtle.bgcolor("black")
t = turtle.Turtle()
t.width(2)
t.speed(0)

color = ('cyan', 'pink', 'white')
for i in range (200):
    t.pencolor(color[i%3])
    t.forward (i*3)
    t.right(121)

turtle.exitonclick()