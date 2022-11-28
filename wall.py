import pygame
from pygame.math import Vector2
from global_values import *

# Welcome to the wall class where most of the wall's logic is located


class WALL:
    def __init__(self):
        """init wall class
        """
        self.make_wall()

    def draw_wall(self, screen):
        """draws the wall as a series of rectangles

        Args:
            screen (_type_): the screen/surface to draw to
        """
        for block in walls:
            # create a rectangle
            x_pos = int(block.x * CELL_SIZE)
            y_pos = int(block.y * CELL_SIZE)
            wall_rect = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, wall_color, wall_rect)

    def make_wall(self):
        """makes the array positions of the walls to draw
        """
        for j in range(1, close_amount+1):
            for i in range(CELL_NUMBER+1):
                walls.append(
                    Vector2(close_amount-j, (CELL_NUMBER-i)))
                walls.append(
                    Vector2(CELL_NUMBER-close_amount-1+j, (CELL_NUMBER-i)))
                walls.append(Vector2((CELL_NUMBER-i), close_amount-j))
                walls.append(
                    Vector2((CELL_NUMBER-i), CELL_NUMBER-close_amount-1+j))

    def update(self, screen):
        self.make_wall()
        self.draw_wall(screen)
