def lozee(n):

    f = n * 2 - 1
    s = 1
    for a in range(n):
        print("\n")
        for i in range(int((f - s)/2)):
            print(" ",end="")
        for b in range(s):
            print("*",end="")
        for i in range(int((f - s)/2)):
            print(" ",end="")
        s = s + 2

    m = n * 2 - 3
    for i in range(n - 1):
        print("\n")
        for i in range(int((f - m)/2)):
            print(" ",end="")
        for p in range(m):
            print("*",end="")
        for i in range(int((f - m)/2)):
            print(" ",end="")
        m = m - 2

lozee(int(input()))