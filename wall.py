
import pygame
from pygame.math import Vector2
from global_values import *
import random
# Welcome to the wall class where most of the wall's logic is located


class WALL:
    def __init__(self):
        """init wall class
        """
        self.wall_increment = 0
        self.close_amount = close.get_close_amount()
        self.make_wall()
        sprite = random.randint(0, 1)
        if sprite == 0:
            self.wall_sprites = [pygame.image.load("Assets/fire1.png").convert_alpha(),
                                 pygame.image.load("Assets/fire2.png").convert_alpha()]
        if sprite == 1:
            self.wall_sprites = [pygame.image.load("Assets/barbwall1.png").convert_alpha(),
                                 pygame.image.load("Assets/barbwall2.png").convert_alpha()]
        self.cycle = 0
        self.cycle_used = 0
        self.cycle_speed = 100
        self.walls = []

    def draw_wall(self, screen):
        """draws the wall as a series of rectangles

        Args:
            screen (_type_): the screen/surface to draw to
        """
        self.close_amount = close.get_close_amount()
        self.cycle_used += 1
        if self.cycle_used <= self.cycle_speed:
            self.cycle = 0
        elif self.cycle_speed <= self.cycle_used <= self.cycle_speed * 2:
            self.cycle = 1
        elif self.cycle_used >= self.cycle_speed * 2:
            self.cycle_used = 0
        for block in self.walls:
            # create a rectangle
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            wall_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            #pygame.draw.rect(screen, wall_color, wall_rect)
            screen.blit(self.wall_sprites[self.cycle], wall_rect)

    def make_wall(self):
        """makes the array positions of the walls to draw
        """
        self.close_amount = close.get_close_amount()
        self.wall_increment += 1
        for j in range(1, self.close_amount+1):
            for i in range(CELL_NUMBER+1):
                self.walls.append(
                    Vector2(self.close_amount-j, (CELL_NUMBER-i)))
                self.walls.append(
                    Vector2(CELL_NUMBER-self.close_amount-1+j, (CELL_NUMBER-i)))
                self.walls.append(
                    Vector2((CELL_NUMBER-i), self.close_amount-j))
                self.walls.append(
                    Vector2((CELL_NUMBER-i), CELL_NUMBER-self.close_amount-1+j))
        # print(len(self.walls))

    def update(self, screen):
        self.draw_wall(screen)
        self.close_amount = close.get_close_amount()
        #print(f"wall Close Amount {self.close_amount}")
