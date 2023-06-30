import random
import arcade

class Spaceship(arcade.Sprite):
    def __init__(self,Game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = Game.width / 2
        self.center_y = 40
        self.width = 50
        self.height = 50
        self.speed = 8

class Enemy(arcade.Sprite):
    def __init__(self,Game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0, Game.width)
        self.center_y = Game.height + 30
        self.width = 60
        self.height = 60
        self.angle = 180
        self.speed = 8

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000,height=700,title="kiya game_test")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        # self.background = arcade.load_texture("Assignment 13\class code\download.jpg")
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.my_jet = Spaceship(self)
        self.doshman = Enemy(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.my_jet.draw()
        self.doshman.draw()

    def on_key_press(self,synbol : int,modifiers: int):
        print("dokme zad")
        print(synbol)
        # a
        if synbol == 97:
            print("left")
            self.my_jet.center_x -= self.my_jet.speed
        # d
        if synbol == 100:
            print("right")
            self.my_jet.center_x += self.my_jet.speed

    def on_update(self, delta_time):
        self.doshman.center_y -= self.doshman.speed


window = Game()

arcade.run()