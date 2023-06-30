import arcade
from bullet import Bullet

class Spaceship(arcade.Sprite):
    def __init__(self,Game):
        super().__init__(":resources:images/space_shooter/playerShip1_blue.png")
        self.center_x = Game.width / 2
        self.center_y = 40
        self.change_x = 0
        self.change_y = 0
        self.width = 50
        self.height = 50
        self.speed = 4
        self.Game_width = Game.width
        self.Bullet_list = []

    def move(self):
        if self.change_x == -1:
            if self.center_x > 0:
                self.center_x -= self.speed
        elif self.change_x == 1:
            if self.center_x < self.Game_width:
                self.center_x += self.speed
                
    def fire(self):
        new_bullet = Bullet(self)
        self.Bullet_list.append(new_bullet)