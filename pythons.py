# https://youtu.be/QFvqStqPCRU main youtube tutorial, most of the logic for the game comes from here
# This is not a copy paste of his work.
# There has been so many alterations to accommodate 2 players and more than 1 fruit
# Also a proper death screen and a wall zone system
# Assets are also handmade by the group

# Only requirement for running the code is pygame
# The version of pygame being developed with is "pygame 2.1.3.dev8 (SDL 2.0.22, Python 3.11.0)"
import pygame
from fruit import *
from snake import *
from game_events import *
from global_values import *
from wall import *
# WATCH THIS to 30:00 or you will be clueless
# https://youtu.be/QFvqStqPCRU?t=226

# initialise the pygame library so it is ready to start drawing the game
pygame.init()

# Creates the main screen with the amount of cells and the size of them
screen = pygame.display.set_mode(
    (CELL_NUMBER * (CELL_SIZE+13), CELL_NUMBER * (CELL_SIZE+1)))

# creates a surface to handle scaling
scale_surface = pygame.Surface((screen.get_width(), screen.get_height()))
# Creates a surface for the main snake game to take place
game_surface = pygame.Surface(
    (CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))

# our main clock
clock = pygame.time.Clock()

# Creates an array of fruit
fruits = []
for i in range(2):
    fruits.append(FRUIT())

# Creates 2 snakes that have to fight and compete to eliminate each other
snake_1 = SNAKE(initial_vector=[Vector2(int(CELL_NUMBER/2+4),
                                        int(CELL_NUMBER/2)),
                                Vector2(int(CELL_NUMBER/2+3),
                                        int(CELL_NUMBER/2)),
                                Vector2(int(CELL_NUMBER/2+2),
                                        int(CELL_NUMBER/2))],
                snakecol=python_blue_color,
                dn="blue Snek")
snake_2 = SNAKE(start_direction=LEFT_VECTOR,
                initial_vector=[Vector2(int(CELL_NUMBER/2-4),
                                        int(CELL_NUMBER/2)),
                                Vector2(int(CELL_NUMBER/2-3),
                                        int(CELL_NUMBER/2)),
                                Vector2(int(CELL_NUMBER/2-2),
                                        int(CELL_NUMBER/2))],
                snakecol=python_yellow_color,
                dn="yellow Snek")
# A wall that will slowly close in, limiting the play area
wall = WALL()
# Screen time timer
pygame.time.set_timer(SCREEN_UPDATE, 120)

# Create the main game loop (all the calculations and stuff happen here)
while True:
    # this rectangle is so we can set the game to be in the center of the screen
    rect = game_surface.get_rect(
        center=(screen.get_width()/2, screen.get_height()/2))
    # FIXME snake clips through itself if you press down and right at the same time or up and left
    # hours wasted = 5
    snake_1.moved = True
    snake_2.moved = True
    # the event loop, captures stuff like keypresses and mouse movement
    for event in pygame.event.get():
        # debug line to see what events are happening
        # print(event)
        quit_game(event)
        # responsible for checking if the snake is colliding with itself or a wall or a fruit
        snake_screen_update(event, [snake_1, snake_2], fruits)
        # moves snake_1 with the arrow keys (blue snek)
        arrow_move(event, snake_1)
        # moves snake_2 with the W/A/S/D keys
        arrow_move(event, snake_2,
                   up=pygame.K_w,
                   down=pygame.K_s,
                   left=pygame.K_a,
                   right=pygame.K_d)

    # gives the scale surface a color (from global_values.py)
    scale_surface.fill(screen_color)
    # fills the (snake game) surface with a color (from global_values.py)
    game_surface.fill(board_color)
    # draws the snakes onto the game_surface
    snake_1.draw_elements(game_surface)
    snake_2.draw_elements(game_surface)
    # draws the fruits to the game_surface
    for i in fruits:
        i.draw_elements(game_surface)
    # draws the walls to the game_surface
    wall.draw_wall(game_surface)
    # blits (puts on top of) the game_surface to the scale surface in the
    # position of the rectangle made at the beginning of the loop (basically the center)
    scale_surface.blit(game_surface, rect)
    # blits the scaled surface onto the main screen in the top left corner
    screen.blit(pygame.transform.scale(
        scale_surface, screen.get_rect().size), (0, 0))
    # actually shows the changes to the player
    pygame.display.update()

    # attempt to fix the snake clipping problem
    snake_1.start_direction = snake_1.previous_direction
    snake_2.start_direction = snake_2.previous_direction
    # sets the game to refresh at the "#" frames per second
    # (this game refreshes at 60 fps)
    clock.tick(60)
