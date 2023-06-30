import threading
import time
import random
import arcade
from spaceship import Spaceship
from enemy import Enemy
from jon import Jon
from bullet import Bullet
from threading import Thread

DEFAULT_FONT_SIZE = 45
    
class Game(arcade.Window):
    def __init__(self):
        self.w = 500
        self.h = 700
        super().__init__(self.w,self.h,title="kiya game_test")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.background = arcade.load_texture("C:/Users/home/Desktop/python class/Pylern/Assignments/Assignment 24/tamrin/Space-Shooter/start.PNG")
        self.next_enemy_time = 3
        self.game_start_time = time.time()
        self.start_time = time.time()
        self.my_jet = Spaceship(self)
        self.tir = Bullet(self.my_jet)
        self.doshmans = []
        self.my_jet.update_jon()
        self.enemy_speed = 2

        self.my_thread = threading.Thread(target=self.new_enemy)
        self.my_thread.start()

    def new_enemy(self):
        while True:
            self.enemy_speed += 0.5
            self.new_doshman = Enemy(self,self.enemy_speed)
            self.doshmans.append(self.new_doshman)
            time.sleep(3)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.width,self.height,self.background)
        self.my_jet.draw()

        arcade.draw_text("Score:",350,20, font_size=20)
        arcade.draw_text(self.my_jet.Score,430,20, font_size=20)

        if len(self.my_jet.jons) <= 0:
            Spaceship.sound()
            exit(0)
            
        for doshman in self.doshmans:
            if arcade.check_for_collision(doshman, self.my_jet):
                self.doshmans.remove(doshman)
                Spaceship.sound()
                exit(0)

        for doshman in self.doshmans:
            doshman.draw()
        
        for jon in self.my_jet.jons:
            jon.draw()
        
        for bullet in self.my_jet.Bullet_list:
            bullet.draw()
        
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.A or symbol == arcade.key.D:
            self.my_jet.change_x = 0

    def on_key_press(self,synbol : int,modifiers: int):
        print("dokme zad")
        print(synbol)
        if synbol == arcade.key.A:
            print("left")
            self.my_jet.change_x = -1
        elif synbol == arcade.key.D:
            print("right")
            self.my_jet.change_x = 1
        elif synbol == arcade.key.SPACE:
            self.background = arcade.load_texture(":resources:images/backgrounds/stars.png")
            self.my_jet.fire()
            self.tir.sound()
    
    def on_update(self, delta_time):

        for bullet in self.my_jet.Bullet_list:
            bullet.move()

        for bullet in self.my_jet.Bullet_list:
            if bullet.center_y > 700:
                self.my_jet.Bullet_list.remove(bullet)

        for doshman in self.doshmans:
            for bullet in self.my_jet.Bullet_list:
                if arcade.check_for_collision(doshman, bullet):
                    self.doshmans.remove(doshman)
                    self.my_jet.Bullet_list.remove(bullet)
                    self.my_jet.Score += 1
        
        for doshman in self.doshmans:
            if doshman.center_y < 0:
                self.doshmans.remove(doshman)
                self.my_jet.jons.remove(self.my_jet.jons[0])

        self.my_jet.move()

    
        for doshman in self.doshmans:  
            doshman.move()

window = Game()
arcade.run()