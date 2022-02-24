# generalization of shape
  
import turtle
pen = turtle.Turtle()

n = int(input("Enter the no of the sides of the polygon : "))
s = int(input("Enter the length of the sides of the polygon : "))
  
  
for _ in range(n):
    turtle.forward(s)
    turtle.right(360 / n)