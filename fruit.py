import pygame
from pygame.math import Vector2
import random
from global_values import *
from game_events import *

# Welcome to the fruit class where most of the fruit logic is located


class FRUIT:
    def __init__(self, color=fruit_color):
        """Runs on Create of the FRUIT object
        """
        # Get an x and y position that doesn't have a snake in it
        self.x = random.randint(close_amount+1, (CELL_NUMBER-close_amount)-2)
        self.y = random.randint(close_amount+1, (CELL_NUMBER-close_amount)-2)
        self.pos = Vector2(self.x, self.y)
        self.color = color

    def draw_fruit(self, screen):
        """Draws the fruit to the screen as a rectangle

        Args:
            screen (pygame.display): The main screen of the Game
        """
        x_pos = int(self.pos.x * CELL_SIZE)
        y_pos = int(self.pos.y * CELL_SIZE)
        # make a rectangle
        fruit_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
        # draw the rectangle
        pygame.draw.rect(screen, self.color, fruit_rect)

    def randomize_fruit(self, snake_pos2, fruit_pos2):
        """places the fruit randomly and tries to avoid placing it inside the snake

        Args:
            snake_pos2 (_type_): an array of every body part of the snake
            fruit_pos2 (_type_): an array of every fruit
        """
        self.x = random.randint(close_amount+1, (CELL_NUMBER-close_amount)-2)
        self.y = random.randint(close_amount+1, (CELL_NUMBER-close_amount)-2)
        self.pos = Vector2(self.x, self.y)
        temp = []
        for i in snake_pos2:
            temp += i
        snake_pos2 = temp

        # if the fruit is inside the snake then randomize it again
        for i in snake_pos2:
            if self.pos == i:
                print("DEBUG: Theres a snake in my fruit!")
                self.randomize_fruit(fruit_pos2, snake_pos2)

        # if the fruit is inside another fruit then randomize it again
        for i in fruit_pos2:
            if self.pos == i:
                print("DEBUG: Fruit In Fruit")
                self.randomize_fruit(fruit_pos2, snake_pos2)

    def draw_elements(self, screen):
        """draws the elements to the screen/surface

        Args:
            screen (_type_): The screen/surface that the fruit should be drawn to
        """
        self.draw_fruit(screen)

    def get_fruit_positions(self):
        """return the position of a fruit

        Returns:
            Vector2: a Vector2 of the fruits position
        """
        return self.pos
