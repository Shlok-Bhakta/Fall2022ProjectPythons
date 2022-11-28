import pygame
from fruit import *
from snake import *
from wall import *
from global_values import *


class MAIN:
    def __init__(self, start_direction=RIGHT_VECTOR, initial_vector=[Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)], snakecol=snake_color):
        self.snake = SNAKE(start_direction, initial_vector, snakecol)
        self.start_direction = self.snake.previous_direction
        self.moved = True

    def update(self):
        self.check_fruit_collision()
        self.check_snake_collision()
        self.snake.move_snake()

    def check_fruit_collision(self):
        for i in fruit_pos:
            if i == self.snake.body[0]:
                # place the fruit randomly on the board
                self.fruit.randomize_fruit()
                while self.fruit.pos in self.snake.body:
                    self.fruit.randomize_fruit()
                    print("redirected FRUIT")
                self.snake.add_block()
                # extend snake

    def check_snake_collision(self):
        if not close_amount <= self.snake.body[0].x < CELL_NUMBER-close_amount:
            self.game_over()
        if not close_amount <= self.snake.body[0].y < CELL_NUMBER-close_amount:
            self.game_over()
        for block in self.snake.body[1:]:
            if self.snake.body[0] == block:
                self.game_over()

    def game_over(self):
        print("Game Over")
