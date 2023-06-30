import qrcode
import pyfiglet

PRODUCTS = []
Cart = []

def read_data():
    f = open("C:/Users/home/Desktop/python class/Assignment 7/tamrin/data.txt","r")

    for line in f:
        result = line.split(",")
        my_dict = {"code": result[0],"name": result[1],"price": result[2], "count": result[3]}

        PRODUCTS.append(my_dict)
    
    f.close()

def show_menu():
    print("1 = Add")
    print("2 = Edit")
    print("3 = Remove")
    print("4 = Serch")
    print("5 = Show")
    print("6 = Buy")
    print("7 = QR_code")
    print("8 = Exit")
    
def Add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")

    new_product = {"code": code,"name":name,"price":price,"count":count}
    PRODUCTS.append(new_product)

def Edit():
    code = input("enter code: ")
    print("name")
    print("price")
    print("count")
    user_input = input()
    new_product = input("input new product: ")

    for product in PRODUCTS:
        if product["code"] == code:
            product[user_input] = new_product
            print("Information updated successfully!!")
            break
    else:
        print("not found")
    print(product)

def Remove():
    a = 0
    code = input("enter code: ")
    for product in PRODUCTS:
        a = a + 1
        if product["code"] == code:
            del PRODUCTS[a-1]
            print("Information Delete successfully!!")
            break
    else:
        print("not found")
    
def QR_code():
    code = input("enter code: ")
    for product in PRODUCTS:
        if product["code"] == code:
            img = qrcode.make(product)
            img.save("product_QR_code.png")
            break
    else:
        print("not found")


def Serch():
    user_input = input("type your keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"],"\t\t",product["name"],"\t\t",product["price"],"\t\t")
            break
    else:
        print("not found")
    
def Show_list():
    print("cod\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"],"\t\t",product["name"],"\t\t",product["price"],"\t\t")
def write_to_date():
    f = open("classcode\data.txt","w")

    for product in PRODUCTS:
        o = product["name"]
        l = product["price"]
        k = product["count"]
        m = product["code"]
        e = m,o,l,int(k)-0

        f.write(f"{str(e)}\n")

    f.close()
def Buy():
    s = []
    p = []
    while True:
        print("1 = stay, 2 = exit")
        user_input = int(input())
        if user_input == 1:
            user_input = input("code: ")
            for product in PRODUCTS:
                if product["code"] == user_input:
                    count = int(input("enter count: "))
                    if int(product["count"]) >= count:
                        s.append(count)
                        b = int(product["price"])*count
                        p.append(b)
                        product["count"] = int(product["count"]) - count
                        o = product["name"]
                        l = product["price"]
                        k = count
                        m = o,l,k,b
                        Cart.append(m)
                        break
                    else:
                        print("Insufficient inventory")
            else:
                print("not found")
        if user_input == 2:
            for product in Cart:
                print(product)
            print("sum count = ",sum(s))
            print("sum price = ",sum(p))
            break

title = pyfiglet.figlet_format("welcome to my store", font="slant")
print(title)
print("loding...")
read_data()
print("Date loaded.")


while True:

    show_menu()

    choice = int(input("enter your choice: "))

    if choice == 1:
        Add()
    elif choice == 2:
        Edit()
    elif choice == 3:
        Remove()
    elif choice == 4:
        Serch()
    elif choice == 5:
        Show_list()
    elif choice == 6:
        Buy()
    elif choice == 7:
        QR_code()
    elif choice == 8:
        write_to_date()
        exit(0)
    else:
        print("dorost vared kon")