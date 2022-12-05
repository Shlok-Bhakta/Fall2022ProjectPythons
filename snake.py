import pygame
from pygame.math import Vector2
from global_values import *
import random
# Welcome to the snake class where most of the snake logic is located


class SNAKE:
    def __init__(self,
                 snake_id,
                 is_ai=False,
                 start_direction=RIGHT_VECTOR,
                 previous_direction=LEFT_VALUE,
                 initial_vector=[Vector2(5, 10), Vector2(
                     4, 10), Vector2(3, 10)],
                 snake_col=snake_color,
                 snake_name="snek",
                 head_path="Assets/bluesnake/snake_head.png",
                 body_path="Assets/bluesnake/Python Game Blue Body.png",
                 corner_path="Assets/bluesnake/Python Game Blue Turn.png",
                 tail_path="Assets/bluesnake/Python Game Blue Tail.png"):
        """Creates a snake

        Args:
            start_direction (Vector2, optional): What direction will the snake start to go in. Defaults to RIGHT_VECTOR.
            initial_vector (list of Vector2, optional): The start positions of the snake. Defaults to [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)].
            snakecol (color, optional): The color of the snake squares. Defaults to snake_color.
            dn (str, optional): A name to help debug the snake. Defaults to "snek".
        """
        self.is_ai = is_ai
        self.ID = snake_id
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
        self.previous_direction = previous_direction
        self.start_direction = self.previous_direction
        self.close_amount = close.get_close_amount()
        self.increment = 0
        self.score = 0
        self.actual_score = 0
        # Importing image assets
        self.head = pygame.image.load(
            head_path).convert_alpha()
        self.mid = pygame.image.load(
            body_path).convert_alpha()
        self.tail = pygame.image.load(
            tail_path).convert_alpha()
        self.turn = pygame.image.load(
            corner_path).convert_alpha()

        self.snake_head = self.head
        self.snake_mid = self.mid
        self.snake_tail = self.mid
        self.snake_turn = self.turn

    def draw_snake(self, screen):
        """Draws the snake to the screen as a series of rectangles

        Args:
            screen (pygame.display): The main screen of the Game
        """
        self.update_head_graphics()
        self.update_tail_graphics()
        for index, block in enumerate(self.body):
            # create a rectangle
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            block_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            # draw rectangle
            if index == 0:
                screen.blit(self.snake_head, block_rect)
            elif index == len(self.body) - 1:
                screen.blit(self.snake_tail, block_rect)
            else:
                previous_block = self.body[index+1]
                next_block = self.body[index-1]
                previous_vector = previous_block - block
                next_vector = next_block - block
                if previous_vector.x == next_vector.x:
                    self.snake_mid = pygame.transform.rotate(self.mid, 90)
                    screen.blit(self.snake_mid, block_rect)
                elif previous_vector.y == next_vector.y:
                    screen.blit(self.mid, block_rect)
                else:
                    if previous_vector.x == -1 and next_vector.y == -1 or previous_vector.y == -1 and next_vector.x == -1:
                        self.snake_turn = pygame.transform.rotate(
                            self.turn, 270)
                        screen.blit(self.snake_turn, block_rect)
                    elif previous_vector.x == -1 and next_vector.y == 1 or previous_vector.y == 1 and next_vector.x == -1:
                        self.snake_turn = pygame.transform.rotate(
                            self.turn, 0)
                        screen.blit(self.snake_turn, block_rect)
                    elif previous_vector.x == 1 and next_vector.y == -1 or previous_vector.y == -1 and next_vector.x == 1:
                        self.snake_turn = pygame.transform.rotate(
                            self.turn, 180)
                        screen.blit(self.snake_turn, block_rect)
                    elif previous_vector.x == 1 and next_vector.y == 1 or previous_vector.y == 1 and next_vector.x == 1:
                        self.snake_turn = pygame.transform.rotate(
                            self.turn, 90)
                        screen.blit(self.snake_turn, block_rect)
            #pygame.draw.rect(screen, self.color, block_rect)

    def update_head_graphics(self):
        head_orientation = self.body[1]-self.body[0]
        if head_orientation == RIGHT_VECTOR:
            self.snake_head = pygame.transform.rotate(self.head, 0)
        elif head_orientation == LEFT_VECTOR:
            self.snake_head = pygame.transform.rotate(self.head, 180)
        elif head_orientation == UP_VECTOR:
            self.snake_head = pygame.transform.rotate(self.head, 90)
        elif head_orientation == DOWN_VECTOR:
            self.snake_head = pygame.transform.rotate(self.head, 270)

    def update_tail_graphics(self):
        tail_orientation = self.body[-2]-self.body[-1]
        if tail_orientation == RIGHT_VECTOR:
            self.snake_tail = pygame.transform.rotate(self.tail, 180)
        elif tail_orientation == LEFT_VECTOR:
            self.snake_tail = pygame.transform.rotate(self.tail, 0)
        elif tail_orientation == UP_VECTOR:
            self.snake_tail = pygame.transform.rotate(self.tail, 270)
        elif tail_orientation == DOWN_VECTOR:
            self.snake_tail = pygame.transform.rotate(self.tail, 90)

    def move_snake(self):
        """Moves the snake in a vector direction
        """
        # print(f"{self.name} is ! ai")
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
            return self.game_over()
        if not self.close_amount <= self.body[0].y < CELL_NUMBER-self.close_amount:
            return self.game_over()
        # check if colliding with itself
        for block in self.body[1:]:
            if self.body[0] == block:
                return self.game_over()
        # check collision with other snakes' bodies
        for block in other_snakes[1:]:
            if self.body[0] == block:
                #print(f"{self.name}: other snake collision detected")
                return self.game_over()
        if self.body[0] == other_snakes[0]:
            #print(f"{self.name}: head collision detected")
            return self.game_over()
        return False, -1
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
        #print("Game Over")
        #print(f"{self.name}: {abs(self.score)}")
        return True, self.ID

    def update(self):
        """updates the snake's collision checking
        """
        self.close_amount = close.get_close_amount()
        # self.check_snake_collision(snakes)
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

    def get_head(self):
        return self.body[0]

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
