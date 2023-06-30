import turtle
import time

colors = ["red","blue","purple","green","yellow","orange"]

turtle.bgcolor("black")

s = turtle.Pen()

i = 0
while i < 360:
    for j in range(len(colors)):
        s.width(i / 100 + 1)
        s.pencolor(colors[j])
        s.forward(i)
        s.left(59)
        i+=1

# s.pencolor("blue")
# s.width(5)

# s.forward(100)
# s.left(90)
# s.forward(100)
# s.left(90)
# s.forward(100)
# s.left(90)
# s.forward(100)


# s.forward(100)
# s.left(120)
# s.forward(100)
# s.left(120)
# s.forward(100)
# s.left(120)

# time.sleep(3)