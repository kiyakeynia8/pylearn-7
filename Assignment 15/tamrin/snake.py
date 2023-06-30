import arcade


class Snake(arcade.Sprite):
    def __init__(self,Game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = Game.width // 2
        self.center_y = Game.height // 2
        self.color = arcade.color.GREEN
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 1
        self.body = []

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)
        arcade.draw_text("Score", 350, 25, arcade.color.BLACK, 20)
        arcade.draw_text(self.score, 430, 23, arcade.color.BLACK, 20)

        a = 1
        for part in self.body:
            if a % 2 == 0:
                arcade.draw_rectangle_filled(part["x"], part["y"], self.width, self.height, arcade.color.BLACK)
                a+=1
            else:
                arcade.draw_rectangle_filled(part["x"], part["y"], self.width, self.height, arcade.color.YELLOW)
                a+=1

    def move(self):
        self.body.append({"x":self.center_x,"y":self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def apple_eat(self,apple_food):
        del apple_food
        self.score += 1

    def rock_eat(self,rock):
        del rock
        self.score -= 1

    def pear_eat(self,pear_food):
        del pear_food
        self.score +=2