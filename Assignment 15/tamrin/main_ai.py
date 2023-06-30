import random
import time
import arcade
from apple import Apple,Pear,Rock
from snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=500, height=500, title="super_snake -- V1")
        arcade.set_background_color(arcade.color.KHAKI)

        self.width = 500
        self.height = 500
        self.snake = Snake(self)
        self.apple_food = Apple(self.width,self.height)
        self.rock = Rock(self.width,self.height)
        self.pear_food = Pear(self.width,self.height)

        self.a = 1

    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple_food.draw()    
        self.rock.draw()
        self.pear_food.draw()
        if self.snake.score <= 0:
            arcade.draw_rectangle_filled(260, 270, 550, 550, arcade.color.BLACK)
            arcade.draw_text("Game over", 150, 250, font_size=40)
        if self.snake.center_x == 0 or self.snake.center_x == self.width or self.snake.center_y == 0 or self.snake.center_x == self.height:
            arcade.draw_rectangle_filled(260, 270, 550, 550, arcade.color.BLACK)
            arcade.draw_text("Game over", 150, 250, font_size=40)
        arcade.finish_render()

    def on_update(self, delta_time):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.rock) or arcade.check_for_collision(self.snake, self.apple_food) or arcade.check_for_collision(self.snake, self.pear_food):
            if arcade.check_for_collision(self.snake, self.apple_food):
                self.snake.apple_eat(self.apple_food)

            if arcade.check_for_collision(self.snake, self.rock):
                self.snake.rock_eat(self.rock)

            if arcade.check_for_collision(self.snake, self.pear_food):
                self.snake.pear_eat(self.pear_food)

            self.a = random.randint(1, 3)
            if self.a == 1:
                self.apple_food = Apple(self.width,self.height)
            if self.a == 2:
                self.rock = Rock(self.width,self.height)
            if self.a == 3:
                self.pear_food == Pear(self.width,self.height)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1
        if symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1
        if symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0
        if symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0

if __name__ == "__main__":
    game = Game()
    arcade.run()