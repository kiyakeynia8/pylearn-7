def setare(n,m):
    h = 0
    l = n
    khat = []
    khat2 = []
    y = n - 1
    s = n % 2
    d = int(n / 2)

    if s == 0:
        
        for i in range(d):
            khat.append("*")
            khat.append("#")

    if s == 1:

        for i in range(n):

            if i < n:
                khat.append("*")
                n = n - 1

            if i < y:
                khat.append("#")
                y = y - 1

    y = l - 1
    s = l % 2
    d = int(l / 2)

    if s == 0:
        
        for i in range(d):
            khat2.append("#")
            khat2.append("*")

    if s == 1:

        for i in range(l):

            if i < l:
                khat2.append("#")
                l = l - 1

            if i < y:
                khat2.append("*")
                y = y - 1

    if m % 2 == 0:
        for i in range(int(m / 2)):
            print(*khat)
            print(*khat2)

    if m % 2 == 1:
        for i in range(int(m)):
            if h < m:
                print(*khat)
                h = h + 1
            else:
                break
            if h < m:
                print(*khat2)
                h = h + 1
            else:
                break

setare(int(input()), int(input()))
            