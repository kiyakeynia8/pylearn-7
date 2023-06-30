import qrcode
import pyfiglet
from Film import Film
from Series import Series
from Documentary import Documentary
from Clip import Clip
from Mediaa import Mediaa


MEDIAS = []

class Media:
    def __init__(self, c, n, dir, imdb, u, dur, cas):
        self.code = c
        self.name = n
        self.director = dir
        self.IMDBscore = imdb
        self.url = u
        self.duration = dur
        self.casts = cas

    @staticmethod
    def Advanced_search():
        print(media.code,"\t\t",media.name,"\t\t",media.director,"\t\t",media.IMDBscore,"\t\t",media.url,"\t\t",media.duration,"\t\t",media.casts,"\t\t",media.N_o_episodes,"\t\t",media.Year_of_construction,"\t\t",media.location,"\t\t",medi.date,"\t\t")
        
    def Add():
        code = input("enter code: ")
        name = input("enter name: ")
        director = input("enter director: ")
        IMDBscore = input("enter IMDB score: ")
        url = input("enter url: ")
        duration = input("enter duration: ")
        casts = input("enter casts: ")
        N_o_episodes = input("enter N_o_episodes: ")
        Year_of_construction = input("enter Year_of_construction: ")
        location = input("enter location: ")
        date = input("enter date: ")

        if Year_of_construction != "...":
            my_obj = Film(code,name,director,IMDBscore,url,duration,casts,N_o_episodes,Year_of_construction,location,date)

        if  N_o_episodes != "...":
            my_obj = Series(code,name,director,IMDBscore,url,duration,casts,N_o_episodes,Year_of_construction,location,date)

        if location != "..." and date != "...":
            my_obj = Documentary(code,name,director,IMDBscore,url,duration,casts,N_o_episodes,Year_of_construction,location,date)

        else:
            my_obj = Clip(code,name,director,IMDBscore,url,duration,casts,N_o_episodes,Year_of_construction,location,date)
        
        MEDIAS.append(my_obj)

    def Edit():
        print("name")
        print("director")
        print("IMDB score")
        print("url")
        print("duration")
        print("casts")
        print("N_o_episodes")
        print("Year_of_construction")
        print("location")
        print("date")
        user_input = input()
        new_media = input("input new product: ")

        media.user_input = new_media
        print("Information updated successfully!!")

    def Remove():
        del MEDIAS[a-1]
        print("Information Delete successfully!!")

    @staticmethod
    def Serch():
        user_input = input("type your keyword: ")
        for media in MEDIAS:
            if media.code == user_input or media.name == user_input:
                print(media.code,"\t\t",media.name,"\t\t",media.director,"\t\t",media.IMDBscore,"\t\t",media.url,"\t\t",media.duration,"\t\t",media.casts,"\t\t",media.N_o_episodes,"\t\t",media.Year_of_construction,"\t\t",media.location,"\t\t",medi.date,"\t\t")
                break
        else:
            print("not found")
        
    @staticmethod
    def Show_list():
        print("code\t\t\tname\t\t\tdirector\t\tIMDB score\t\t\turl\t\t\t\tduration\t\t\tcasts\t\t\t")
        for media in MEDIAS:
            print(media.code,"\t\t",media.name,"\t\t",media.director,"\t\t",media.IMDBscore,"\t\t",media.url,"\t\t",media.duration,"\t\t",media.casts,"\t\t",media.N_o_episodes,"\t\t",media.Year_of_construction,"\t\t",media.location,"\t\t",medi.date,"\t\t")
    
    def write_to_date():
        p = open("Assignment 12/tamrin/data.txt","w")

        for media in MEDIAS:
            m = media.code
            o = media.name
            l = media.director
            k = media.IMDBscore
            u = media.url
            g = media.duration
            j = media.casts
            e = m,o,l,k,u,g,j

            p.write(f"{e}\n")

        p.close()

def show_menu():
    print("1 = Add")
    print("2 = Edit")
    print("3 = Remove")
    print("4 = Serch")
    print("5 = Show")
    print("6 = Advanced_search")
    print("7 = QR_code")
    print("8 = Exit")

def read_data():
    f = open("Assignment 12/tamrin/data.txt","r")

    for line in f:
        result = line.split(",")

        if result[8] != "...":
            my_obj = Film(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10])

        if result[7] != "...":
            my_obj = Series(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10])

        if result[9] != "..." and result[10] != "...":
            my_obj = Documentary(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10])
        
        else:
            my_obj = Clip(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10])
       
        MEDIAS.append(my_obj)

    f.close()

def QR_code():
    code = input("enter code: ")
    for media in MEDIAS:
        if media.code == code:
            img = qrcode.make(media)
            img.save("product_QR_code.png")
            break
    else:
        print("not found")

title = pyfiglet.figlet_format("welcome to my Media management", font="slant")
print(title)
print("loding...")
read_data()
print("Date loaded.")

while True:
    show_menu()
    choice = int(input("enter your choice: "))
    if choice == 1:
        Media.Add()

    elif choice == 2:
        code = input("enter code: ")
        for media in MEDIAS:
            if int(media.code) == code:
                Media.Edit()
                break
        else:
            print("not found")

    elif choice == 3:
        a = 0
        code = input("enter code: ")
        for media in MEDIAS:
            a = a + 1
            if media.code == code:
                Media.Remove()
                break
        else:
            print("not found")

    elif choice == 4:
        PrMediaoduct.Serch()

    elif choice == 5:
        Media.Show_list()

    elif choice == 6:
        user_input1 = int(input("enter time1: "))
        user_input2 = int(input("enter time2: "))
        for media in MEDIAS:
            if user_input1 <= int(media.duration) <= user_input2:
                media.Advanced_search()
                break
        else:
            print("not found")

    elif choice == 7:
        QR_code()

    elif choice == 8:
        Media.write_to_date()
        exit(0)
        
    else:
        print("dorost vared kon")