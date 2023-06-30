import random
boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]

results = []

for i in range(len(girls)):
    b = random.choice(boys)
    g = random.choice(girls)
    results.append([b,g])
    boys.remove(b)
    girls.remove(g)

    if len(boys) == 1:
        print("single:",boys[0])
        break

    if len (girls) == 1:
        print("single:",girls[0])
        break
    
print(results)