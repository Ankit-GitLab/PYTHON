import turtle

t = turtle.Turtle()
sides = 6           # change value for different polygon
length = 100

angle = 360 / sides

for i in range(sides):
    t.forward(length)
    t.right(angle)

turtle.done()
