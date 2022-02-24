import turtle

t = turtle.Turtle()
turtle.bgcolor("#8BD9E8")
t.pensize(3)
t.color("green")

t.left(90)
t.backward(100)

t.speed(0)

def tree (i):
    if i<10:
        return 
    else:
        t.forward(i)
        t.color("#F03093")
        t.circle(2)
        t.color("green")
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)
tree(100)
turtle.done()
