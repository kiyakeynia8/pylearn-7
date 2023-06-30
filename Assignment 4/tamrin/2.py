user_number = int(input())

s = 1

while True:
    for i in range(user_number):
        s = s * (i+1)
        if s == user_number:
            print("yes")
            exit()
        if s > user_number:
            print("no")
            exit()
