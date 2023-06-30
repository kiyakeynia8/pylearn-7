import time
import random
import arcade
from spaceship import Spaceship
from enemy import Enemy

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500,height=700,title="kiya game_test")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture("Assignment 13/tamrin/start.PNG")

        self.my_jet = Spaceship(self)
        self.doshmans = []

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.my_jet.draw()
        for doshman in self.doshmans:
            doshman.draw()
        for bullet in self.my_jet.Bullet_list:
            bullet.draw()

    def on_key_release(self, symbol, modifiers):
        self.my_jet.change_x = 0

    def on_key_press(self,synbol : int,modifiers: int):
        global po
        print("dokme zad")
        print(synbol)
        if synbol == arcade.key.A:
            print("left")
            self.my_jet.change_x = -1
        elif synbol == arcade.key.D:
            print("right")
            self.my_jet.change_x = 1
        elif synbol == arcade.key.SPACE:
            po = "space"
            self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
            self.my_jet.fire()

    def on_update(self, delta_time):
        for bullet in self.my_jet.Bullet_list:
            bullet.move()

        for doshman in self.doshmans:
            for bullet in self.my_jet.Bullet_list:
                if arcade.check_for_collision(doshman, bullet):
                    self.doshmans.remove(doshman)
                    self.my_jet.Bullet_list.remove(bullet)

        for doshman in self.doshmans:
            if doshman.center_y < 0:
                self.doshmans.remove(doshman)
 
        for doshman in self.doshmans:
            if arcade.check_for_collision(doshman, self.my_jet):
                print("Game Over")
                exit(0)

        self.my_jet.move()
        
        for doshman in self.doshmans:
            doshman.move()

        if random.randint(1, 80) == 6:
            self.new_doshman = Enemy(self)
            self.doshmans.append(self.new_doshman)

window = Game()

arcade.run()