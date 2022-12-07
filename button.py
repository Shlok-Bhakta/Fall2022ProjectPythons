import pygame
from global_values import *


class BUTTON():
    def __init__(self, image, scale, value):
        """inits a clickable button

        Args:
            image (_type_): _description_
            scale (_type_): _description_
            value (_type_): _description_
        """
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.clicked = False
        self.val = value

    def draw(self, screen, x, y):
        """draws the button

        Args:
            screen (_type_): _description_
            x (_type_): _description_
            y (_type_): _description_

        Returns:
            _type_: _description_
        """
        action = self.mouse()

        self.rect.center = (x, y)
        screen.blit(self.image, self.rect)
        return action

    def mouse(self):
        """gets if its clicked

        Returns:
            _type_: _description_
        """
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
