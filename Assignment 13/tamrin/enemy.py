import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self,Game):
        super().__init__(":resources:images/space_shooter/playerShip1_orange.png")
        self.center_x = random.randint(0, Game.width)
        self.center_y = Game.height + 30
        self.width = 60
        self.height = 60
        self.angle = 180
        self.speed = 2

    def move(self):
        self.center_y -= self.speed