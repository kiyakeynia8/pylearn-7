import turtle
turtle.bgcolor("black")
s = turtle.Pen()

t = 3
z = int(360 / t)
i = 10
s.shape("turtle")
s.shapesize(0.5)
while i < 150:
    for j in range(t):
        s.pencolor("white")
        s.forward(i)
        s.left(z)
        z = int(360 / t)
    i+=10  
    t = t + 1