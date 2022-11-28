import pygame
from pygame.math import Vector2
# size and number of cells
CELL_NUMBER = 29
CELL_SIZE = 32

# screen update event
SCREEN_UPDATE = pygame.USEREVENT

# values to make sure the snake doesn't collide with itself (should *cough* *cough)
UP_VALUE = 1
DOWN_VALUE = 2
LEFT_VALUE = 3
RIGHT_VALUE = 4

# an array of all the wall positions
walls = []
# how closed the wall should be.
# Try changing this to something bigger than 0
# and run pythons.py and see what happens ;)
close_amount = 0

# The colors of the game
screen_color = (10, 200, 70)
board_color = (175, 215, 70)
fruit_color = (126, 166, 140)
snake_color = (100, 10, 10)
python_blue_color = (56, 110, 157)
python_yellow_color = (254, 216, 71)
wall_color = (10, 200, 10)

# an attempt to fix the snake clipping
right = False
left = False
up = False
down = False
DOWN_VECTOR = Vector2(0, 1)
UP_VECTOR = Vector2(0, -1)
LEFT_VECTOR = Vector2(-1, 0)
RIGHT_VECTOR = Vector2(1, 0)

# arrays that know what spaces are filled with snakes and fruit
fruit_pos = []
snake_pos = []
