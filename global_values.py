import pygame
from pygame.math import Vector2
from close_amount import *
from total_score import *
from is2p import *
# size and number of cells
CELL_NUMBER = 29
CELL_SIZE = 32
# Thickness of the border around the game
BORDER_THICKNESS = 10
# screen update event
SCREEN_UPDATE = pygame.USEREVENT
WALL_UPDATE = pygame.USEREVENT + 1
SPEED_SPAWN = pygame.USEREVENT + 2
SLOW_SPAWN = pygame.USEREVENT + 3
# values to make sure the snake doesn't collide with itself (should *cough* *cough)
UP_VALUE = 1
DOWN_VALUE = 2
LEFT_VALUE = 3
RIGHT_VALUE = 4

# how closed the wall should be.
# Try changing this to something bigger than 0
# and run pythons.py and see what happens ;)
# creates a wall close amount
close = CLOSE_AMOUNT(initial_amount=0)
wall_cutoff = 7

# creates a score
score = TOTAL_SCORE(0, 0)

# creates a 2player flag
p2 = IS2P(True)

# The colors of the game
screen_color = (180, 215, 70)
board_color = (175, 215, 70)
grass_color = (167, 209, 61)
fruit_color = (126, 166, 140)
snake_color = (100, 10, 10)
python_blue_color = (56, 110, 157)
python_yellow_color = (254, 216, 71)
wall_color = (10, 200, 10)
speed_color = (245, 0, 253)
slow_color = (0, 255, 255)
border_color = (0, 0, 0)
text_color = (0, 0, 0)
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
speed_pos = []
slow_pos = []

# maximum amount of powerups
max_speed = 1
max_slow = 1

# audio
apple_eat_sfx_path = "Assets/audio/apple.wav"
die_sfx_path = "Assets/audio/die.wav"
change_sfx_path = "Assets/audio/mode_change.wav"
powerup_sound = "Assets/audio/powerup.wav"
closing_sound = "Assets/audio/close.wav"
