
import turtle
pen = turtle.Turtle()
n = int(input("Enter the no of the sides of the polygon : "))
s = int(input("Enter the length of the sides of the polygon : "))
pen.color ("blue", "cyan") 

pen.begin_fill() 
for _ in range(n):
    
    pen.forward(s)
    pen.right(360 / n) 
pen.end_fill()

turtle.exitonclick()    
