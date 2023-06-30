import random
import arcade

class Spaceship(arcade.Sprite):
    def __init__(self,Game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = Game.width / 2
        self.center_y = 40
        self.change_x = 0
        self.change_y = 0
        self.width = 50
        self.height = 50
        self.speed = 2

    def move(self):
        if self.change_x == -1:
            self.center_x -= self.speed
        elif self.center_y == 1:
            self.center_x += self.speed

class Enemy(arcade.Sprite):
    def __init__(self,Game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0, Game.width)
        self.center_y = Game.height + 30
        self.width = 60
        self.height = 60
        self.angle = 180
        self.speed = 4

    def move(self):
        self.center_y -= self.speed

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500,height=700,title="kiya game_test")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        # self.background = arcade.load_texture("Assignment 13\class code\download.jpg")
        self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
        self.my_jet = Spaceship(self)
        self.doshmans = []

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.my_jet.draw()
        for doshman in self.doshmans:
            doshman.draw()

    def on_key_press(self,synbol : int,modifiers: int):
        print("dokme zad")
        print(synbol)
        if synbol == arcade.key.A:
            print("left")
            self.change_x = -1
        elif synbol == arcade.key.D:
            print("right")
            self.change_x = 1
        elif synbol == arcade.key.SPACE:
            ...

    def on_update(self, delta_time):
        self.my_jet.move()
        
        for doshman in self.doshmans:
            doshman.move()

        if random.randint(1, 80) == 6:
            self.new_doshman = Enemy(self)
            self.doshmans.append(self.new_doshman)

window = Game()

arcade.run()