number = []
l = []

while True:
    a = float(input("enter number: "))
    b = input("are you stay? (yes or no ?) ")

    if b == "yes":
        number.append(a)
    
    if b == "no":
        number.append(a)
        print(number)
    
        if len(number) == 1:
            print("List size = 1")
            exit()
    
        for i in range(len(number)-1):
            x = number[i]
            y = number[i+1]
    
            if x <= y:
                l.append("true")
            if x > y:
                l.append("false")

        if "false" in l:
            print("false")
            exit()
        else:
            print("true")
            exit()
                
            

