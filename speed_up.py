import pygame
from pygame.math import Vector2
import random
from global_values import *
from game_events import *

# Welcome to the speed_power class where most of the speed_power logic is located


class SPEED_POWER:
    def __init__(self, color=speed_color):
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
        self.speed_power = []
        self.power_up = []
        self.speed_icon = pygame.image.load(
            "Assets/speedup.png").convert_alpha()

    def draw_speed_power(self, screen):
        """Draws the speed_power to the screen as a rectangle

        Args:
            screen (pygame.display): The main screen of the Game
        """
        self.out_speed_power()
        x_pos = int(self.pos.x * CELL_SIZE)
        y_pos = int(self.pos.y * CELL_SIZE)
        # make a rectangle
        speed_power_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
        # draw the rectangle
        #pygame.draw.rect(screen, self.color, speed_power_rect)
        screen.blit(self.speed_icon, speed_power_rect)

    def randomize_speed_power(self, snake_pos2, speed_power_pos2):
        """places the speed_power randomly and tries to avoid placing it inside the snake

        Args:
            snake_pos2 (_type_): an array of every body part of the snake
            speed_power_pos2 (_type_): an array of every speed_power
        """
        self.snake = snake_pos2
        self.speed_power = speed_power_pos2
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

        # if the speed_power is inside the snake then randomize it again
        for i in snake_pos2:
            if self.pos == i:
                print("DEBUG: Theres a snake in my speed_power!")
                self.randomize_speed_power(speed_power_pos2, snake_pos2)

        # if the speed_power is inside another speed_power then randomize it again
        for i in speed_power_pos2:
            if self.pos == i:
                print("DEBUG: speed_power In speed_power")
                self.randomize_speed_power(speed_power_pos2, snake_pos2)

    def draw_elements(self, screen):
        """draws the elements to the screen/surface

        Args:
            screen (_type_): The screen/surface that the speed_power should be drawn to
        """

        self.draw_speed_power(screen)

    def get_speed_power_positions(self):
        """return the position of a speed_power

        Returns:
            Vector2: a Vector2 of the speed_powers position
        """
        return self.pos

    def out_speed_power(self):
        global CELL_NUMBER
        self.close_amount = close.get_close_amount()-1
        # print("outpower")
        if not self.close_amount <= self.pos.x < CELL_NUMBER-self.close_amount:
            self.randomize_speed_power(self.snake, self.speed_power)
        if not self.close_amount <= self.pos.y < CELL_NUMBER-self.close_amount:
            self.randomize_speed_power(self.snake, self.speed_power)
