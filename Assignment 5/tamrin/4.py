def mosalas(n):
    satr = []

    for i in range(n):
        satr.append([1]*(i+1))

    for i in range(2,n):
        for m in range(1,i):
            satr[i][m] = satr[i-1][m-1] + satr[i-1][m]
    
    for khat in satr:
        print(*khat)

mosalas(int(input()))