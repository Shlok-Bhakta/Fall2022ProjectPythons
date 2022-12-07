import pygame
from pygame.math import Vector2
import random
from global_values import *
from game_events import *

# Welcome to the fruit class where most of the fruit logic is located


class FRUIT:
    def __init__(self, id=0, color=fruit_color):
        """Runs on Create of the FRUIT object
        """
        # Get an x and y position that doesn't have a snake in it
        self.close_amount = close.get_close_amount()
        self.x = random.randint(self.close_amount,
                                (CELL_NUMBER-self.close_amount)-1)
        self.y = random.randint(self.close_amount,
                                (CELL_NUMBER-self.close_amount)-1)
        self.pos = Vector2(self.x, self.y)
        self.color = color
        self.snake = []
        self.fruit = []
        self.id = id
        self.apple_icon = pygame.image.load("Assets/apple.png").convert_alpha()
        self.orange_icon = pygame.image.load(
            "Assets/Python Game Orange.png").convert_alpha()
        self.grapes_icon = pygame.image.load(
            "Assets/Python Game Grapes.png").convert_alpha()
        self.banana_icon = pygame.image.load(
            "Assets/banana.png").convert_alpha()
        self.icons = [self.apple_icon, self.orange_icon,
                      self.grapes_icon, self.banana_icon]
        self.fruit_num = random.randint(0, len(self.icons)-1)

    def draw_fruit(self, screen):
        """Draws the fruit to the screen as a rectangle

        Args:
            screen (pygame.display): The main screen of the Game
        """
        self.out_fruit()
        x_pos = int(self.pos.x * CELL_SIZE)
        y_pos = int(self.pos.y * CELL_SIZE)
        # make a rectangle
        fruit_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
        # draw the rectangle
        #pygame.draw.rect(screen, self.color, fruit_rect)
        screen.blit(self.icons[self.fruit_num], fruit_rect)

    def randomize_fruit(self, snake_pos2, fruit_pos2):
        """places the fruit randomly and tries to avoid placing it inside the snake

        Args:
            snake_pos2 (_type_): an array of every body part of the snake
            fruit_pos2 (_type_): an array of every fruit
        """
        self.snake = snake_pos2
        self.fruit = fruit_pos2
        self.close_amount = close.get_close_amount()
        self.fruit_num = random.randint(0, len(self.icons)-1)
        self.x = random.randint(self.close_amount,
                                (CELL_NUMBER-self.close_amount)-1)
        self.y = random.randint(self.close_amount,
                                (CELL_NUMBER-self.close_amount)-1)
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

    def out_fruit(self):
        """checks if the fruit is outside the bounds
        """
        global CELL_NUMBER
        self.close_amount = close.get_close_amount()
        if not self.close_amount <= self.pos.x < CELL_NUMBER-self.close_amount:
            self.randomize_fruit(self.snake, self.fruit)
        if not self.close_amount <= self.pos.y < CELL_NUMBER-self.close_amount:
            self.randomize_fruit(self.snake, self.fruit)
