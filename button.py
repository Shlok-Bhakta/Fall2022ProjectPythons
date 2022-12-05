import pygame
from global_values import *


class BUTTON():
    def __init__(self, image, scale, value):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.clicked = False
        self.val = value

    def draw(self, screen, x, y):
        action = self.mouse()

        self.rect.center = (x, y)
        screen.blit(self.image, self.rect)
        return action

    def mouse(self):
        action = False
        pos = pygame.mouse.get_pos()
        # print(pos)
        # check mouse_over and clicked
        if self.rect.collidepoint(pos):
            # print("hover")
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        return action
