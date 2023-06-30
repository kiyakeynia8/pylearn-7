import arcade
class Jon(arcade.Sprite):
    def __init__(self,x):
        super().__init__("C:/Users/home/Desktop/python class/Pylern/Assignments/Assignment 24/tamrin/Space-Shooter/love.png")
        self.center_x = x
        self.center_y = 25
        self.width = 50
        self.height = 50