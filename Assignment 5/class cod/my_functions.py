import math

def say_hello(name):
    print("hello",name)

"--------------------"

def tab(a,b,c):
    x = b**2 -4*a*c 

    if x > 0:
        x1 = (-b-math.sqrt(x)) / (2 * a)
        x2 = (-b+math.sqrt(x)) / (2 * a)
        print(x1, x2)

    elif x == 0:
        x = -b / (2*a)
        print(x)

    # else:
    elif x < 0:
        print("no answer")

