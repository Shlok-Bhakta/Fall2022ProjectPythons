import pygame
from pygame.math import Vector2
import random
from global_values import *
from game_events import *

# Welcome to the slow_power class where most of the slow_power logic is located


class SLOW_POWER:
    def __init__(self, color=slow_color):
        """Runs on Create of the Speed Power object
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
        self.slow_power = []
        self.power_up = []

    def draw_slow_power(self, screen):
        """Draws the slow_power to the screen as a rectangle

        Args:
            screen (pygame.display): The main screen of the Game
        """
        self.out_slow_power()
        x_pos = int(self.pos.x * CELL_SIZE)
        y_pos = int(self.pos.y * CELL_SIZE)
        # make a rectangle
        slow_power_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
        # draw the rectangle
        pygame.draw.rect(screen, self.color, slow_power_rect)

    def randomize_slow_power(self, snake_pos2, slow_power_pos2):
        """places the slow_power randomly and tries to avoid placing it inside the snake

        Args:
            snake_pos2 (_type_): an array of every body part of the snake
            slow_power_pos2 (_type_): an array of every slow_power
        """
        self.snake = snake_pos2
        self.slow_power = slow_power_pos2
        self.close_amount = close.get_close_amount()
        self.x = random.randint(self.close_amount,
                                (CELL_NUMBER-self.close_amount)-1)
        self.y = random.randint(self.close_amount,
                                (CELL_NUMBER-self.close_amount)-1)
        self.pos = Vector2(self.x, self.y)
        temp = []
        for i in snake_pos2:
            temp += i
        snake_pos2 = temp

        # if the slow_power is inside the snake then randomize it again
        for i in snake_pos2:
            if self.pos == i:
                print("DEBUG: Theres a snake in my slow_power!")
                self.randomize_slow_power(slow_power_pos2, snake_pos2)

        # if the slow_power is inside another slow_power then randomize it again
        for i in slow_power_pos2:
            if self.pos == i:
                print("DEBUG: slow_power In slow_power")
                self.randomize_slow_power(slow_power_pos2, snake_pos2)

    def draw_elements(self, screen):
        """draws the elements to the screen/surface

        Args:
            screen (_type_): The screen/surface that the slow_power should be drawn to
        """

        self.draw_slow_power(screen)

    def get_slow_power_positions(self):
        """return the position of a slow_power

        Returns:
            Vector2: a Vector2 of the slow_powers position
        """
        return self.pos

    def out_slow_power(self):
        global CELL_NUMBER
        self.close_amount = close.get_close_amount()-1
        # print("outpower")
        if not self.close_amount <= self.pos.x < CELL_NUMBER-self.close_amount:
            self.randomize_slow_power(self.snake, self.slow_power)
        if not self.close_amount <= self.pos.y < CELL_NUMBER-self.close_amount:
            self.randomize_slow_power(self.snake, self.slow_power)
