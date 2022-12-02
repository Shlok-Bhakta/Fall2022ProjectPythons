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
        self.moved = False
        self.speed = 1
        self.default_speed = 1
        self.boosted_speed = 0
        self.slow_speed = 4
        self.boost_spent = 0
        self.boosted_tiles = 20
        self.slow_spent = 0
        self.slow_tiles = 15
        self.last_movement = start_direction
        # Up is 1
        # Down is 2
        # Left is 3
        # Right is 4
        self.previous_direction = RIGHT_VALUE
        self.start_direction = self.previous_direction
        self.close_amount = close.get_close_amount()
        self.increment = 0

        # Importing image assets
        self.head = pygame.image.load(
            "Assets/bluesnake/snake_head.png").convert_alpha()
        self.mid = pygame.image.load(
            "Assets/bluesnake/Python Game Blue Body.png").convert_alpha()
        self.tail = pygame.image.load(
            "Assets/bluesnake/Python Game Blue Tail.png").convert_alpha()
        self.turn = pygame.image.load(
            "Assets/bluesnake/Python Game Blue Turn.png").convert_alpha()

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

        self.correct_movement()
        if self.increment >= self.speed:
            self.last_movement = self.direction
            if self.new_block == True:
                body_copy = self.body[:]
            else:
                body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy
            self.new_block = False
            self.increment = 0
            if self.speed == self.boosted_speed:
                self.boost()
            if self.speed == self.slow_speed:
                self.slow()
        else:
            self.increment += 1

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

    def correct_movement(self):
        if self.direction == DOWN_VECTOR and self.last_movement == UP_VECTOR:
            self.direction = UP_VECTOR
        if self.direction == UP_VECTOR and self.last_movement == DOWN_VECTOR:
            self.direction = DOWN_VECTOR
        if self.direction == LEFT_VECTOR and self.last_movement == RIGHT_VECTOR:
            self.direction = RIGHT_VECTOR
        if self.direction == RIGHT_VECTOR and self.last_movement == LEFT_VECTOR:
            self.direction = LEFT_VECTOR

    def game_over(self):
        """does an action on game_over
        """
        print("Game Over")

    def update(self, other_snake):
        """updates the snake's collision checking
        """
        self.close_amount = close.get_close_amount()
        self.check_snake_collision(other_snake)
        self.move_snake()
        # print(f"{self.name} update snek")

    def get_snake_positions(self):
        """returns a Vector2 array of the snake's positions

        Returns:
            list[Vector2]: Vector2 array of the snake positions
        """
        return self.body

    def get_direction(self):
        return self.direction

    def get_snake_moved(self):
        return self.moved

    def set_snake_moved(self, input: bool):
        self.moved = input

    def boost(self):
        self.speed = self.boosted_speed
        if self.boost_spent <= self.boosted_tiles:
            self.boost_spent += 1
        else:
            self.speed = self.default_speed
            self.boost_spent = 0

    def slow(self):
        self.speed = self.slow_speed
        if self.slow_spent <= self.slow_tiles:
            self.slow_spent += 1
        else:
            self.speed = self.default_speed
            self.slow_spent = 0
