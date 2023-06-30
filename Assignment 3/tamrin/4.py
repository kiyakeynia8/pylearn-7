x = int(input())
y = x - 1
s = x % 2
d = int(x / 2)

if s == 0:
    
    for i in range(d):
        print("*",end= "")
        print("#",end= "")

if s == 1:

    for i in range(x):

        if i < x:
            print("*",end= "")
            x = x - 1

        if i < y:
            print("#",end= "")
            y = y - 1
