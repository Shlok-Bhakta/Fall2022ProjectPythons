import pygame
from pygame.math import Vector2
from global_values import *

# Welcome to the snake class where most of the snake logic is located


class SNAKE:
    def __init__(self, start_direction=RIGHT_VECTOR, initial_vector=[Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)], snake_col=snake_color, snake_name="snek"):
        """Creates a snake

        Args:
            start_direction (Vector2, optional): What direction will the snake start to go in. Defaults to RIGHT_VECTOR.
            initial_vector (list of Vector2, optional): The start positions of the snake. Defaults to [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)].
            snakecol (color, optional): The color of the snake squares. Defaults to snake_color.
            dn (str, optional): A name to help debug the snake. Defaults to "snek".
        """
        self.name = snake_name
        self.body = initial_vector
        self.direction = start_direction
        self.new_block = False
        self.color = snake_col
        self.moved = True
        # Up is 1
        # Down is 2
        # Left is 3
        # Right is 4
        self.previous_direction = RIGHT_VALUE
        self.start_direction = self.previous_direction
        self.close_amount = close.get_close_amount()

    def draw_snake(self, screen):
        """Draws the snake to the screen as a series of rectangles

        Args:
            screen (pygame.display): The main screen of the Game
        """
        for block in self.body:
            # create a rectangle
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            snake_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, self.color, snake_rect)
            # draw rectangle

    def move_snake(self):
        """Moves the snake in a vector direction
        """

        global moved
        if self.new_block == True:
            body_copy = self.body[:]
        else:
            body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy
        self.new_block = False

    def add_block(self):
        """makes the snake increase by one size
        """
        self.new_block = True

    def draw_elements(self, screen):
        """draws the elements of the snake

        Args:
            screen (_type_): the main screen/surface
        """
        self.draw_snake(screen)

    def check_snake_collision(self, other_snakes):
        """Checks to see if the snake collides with itself
        """
        # check if colliding with the walls (cheating by using the dimensions of the board))
        if not self.close_amount <= self.body[0].x < CELL_NUMBER-self.close_amount:
            self.game_over()
        if not self.close_amount <= self.body[0].y < CELL_NUMBER-self.close_amount:
            self.game_over()
        # check if colliding with itself
        for block in self.body[1:]:
            if self.body[0] == block:
                self.game_over()
        # check collision with other snakes' bodies
        for block in other_snakes[1:]:
            if self.body[0] == block:
                print(f"{self.name}: other snake collision detected")
        if self.body[0] == other_snakes[0]:
            print(f"{self.name}: head collision detected")

        #print("collision checked")

    def game_over(self):
        """does an action on game_over
        """
        print("Game Over")

    def update(self, other_snake):
        """updates the snake's collision checking
        """
        self.check_snake_collision(other_snake)
        self.move_snake()
        self.close_amount = close.get_close_amount()
        # print(f"{self.name} update snek")

    def get_snake_positions(self):
        """returns a Vector2 array of the snake's positions

        Returns:
            list[Vector2]: Vector2 array of the snake positions
        """
        return self.body
