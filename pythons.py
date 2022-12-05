# https://youtu.be/QFvqStqPCRU main youtube tutorial, most of the logic for the game comes from here
# This is not a copy paste of his work.
# There has been so many alterations to accommodate 2 players and more than 1 fruit
# Also a proper death screen and a wall zone system
# Assets are also handmade by the group

# Only requirement for running the code is pygame
# The version of pygame being developed with is "pygame 2.1.3.dev8 (SDL 2.0.22, Python 3.11.0)"
import pygame
import time
from close_amount import *
from draw_slow import *
from draw_speed import *
from fruit import *
from game_events import *
from global_values import *
from slow_down import *
from snake import *
from speed_up import *
from wall import *

# WATCH THIS to 30:00 or you will be clueless
# https://youtu.be/QFvqStqPCRU?t=226

# initialise the pygame library so it is ready to start drawing the game


def main(screen):
    close.set_close_amount(0)
    # pygame.init()
    # creates a surface to handle scaling
    scale_surface = pygame.Surface((screen.get_width(), screen.get_height()))
    # Creates a surface for the main snake game to take place
    border_surface = pygame.Surface(
        ((CELL_NUMBER * CELL_SIZE)+BORDER_THICKNESS,
            (CELL_NUMBER * CELL_SIZE)+BORDER_THICKNESS))
    game_surface = pygame.Surface(
        (CELL_NUMBER * CELL_SIZE, CELL_NUMBER * CELL_SIZE))
    # our main clock
    clock = pygame.time.Clock()

    # Creates an array of fruit
    fruits = []
    for i in range(2):
        fruits.append(FRUIT(id=i))

    # speed_power = []
    # for i in range(1):
    #     speed_power.append(SPEED_POWER())

    # slow_power = []
    # for i in range(1):
    #     slow_power.append(SLOW_POWER())
    # Creates 2 snakes that have to fight and compete to eliminate each other
    snake_1 = SNAKE(0,
                    initial_vector=[Vector2(int(CELL_NUMBER/2+4),
                                            int(CELL_NUMBER/2)),
                                    Vector2(int(CELL_NUMBER/2+3),
                                            int(CELL_NUMBER/2)),
                                    Vector2(int(CELL_NUMBER/2+2),
                                            int(CELL_NUMBER/2))],
                    snake_col=python_blue_color,
                    snake_name="Blue")
    snake_2 = SNAKE(1,
                    start_direction=LEFT_VECTOR,
                    previous_direction=LEFT_VALUE,
                    initial_vector=[Vector2(int(CELL_NUMBER/2-4),
                                            int(CELL_NUMBER/2)),
                                    Vector2(int(CELL_NUMBER/2-3),
                                            int(CELL_NUMBER/2)),
                                    Vector2(int(CELL_NUMBER/2-2),
                                            int(CELL_NUMBER/2))],
                    is_ai=True,
                    snake_col=python_yellow_color,
                    snake_name="Yellow",
                    head_path="Assets/yellowsnake/Python Game Yellow Head.png",
                    body_path="Assets/yellowsnake/Python Game Yellow Body.png",
                    corner_path="Assets/yellowsnake/Python Game Yellow Turn.png",
                    tail_path="Assets/yellowsnake/Python Game Yellow Tail.png"
                    )

    # A wall that will slowly close in, limiting the play area
    wall = WALL()

    # Screen time timer
    # temptime = 2000
    temptime = random.randint(0, 5000) * random.randint(0, 50)
    # temptime2 = 2000
    temptime2 = random.randint(0, 5000) * random.randint(0, 50)
    pygame.time.set_timer(SCREEN_UPDATE, 60)
    pygame.time.set_timer(WALL_UPDATE, 4500)
    pygame.time.set_timer(SPEED_SPAWN, temptime)
    pygame.time.set_timer(SLOW_SPAWN, temptime2)
    # draw_speed = DRAW_SPEED(False)
    # draw_slow = DRAW_SLOW(False)
    speed_power = []
    slow_power = []
    game_over = False
    snake_id = -1
    font = pygame.font.Font('Assets/fonts/OpenSans-SemiBold.ttf', 32)
    blue_snake_text = font.render(
        f'{score.get_blue_score()}', True, text_color)
    yellow_snake_text = font.render(
        f'{score.get_yellow_score()}', True, text_color)
    blue_snake_icon = pygame.image.load(
        "Assets/bluesnake/snake_head.png").convert_alpha()
    yellow_snake_icon = pygame.image.load(
        "Assets/yellowsnake/Python Game Yellow Head.png").convert_alpha()
    game_title_icon = pygame.image.load(
        "Assets/Title.png").convert_alpha()
    # Create the main game loop (all the calculations and stuff happen here)
    while True:
        # this rectangle is so we can set the game to be in the center of the screen

        # the event loop, captures stuff like keypresses and mouse movement
        for event in pygame.event.get():
            # debug line to see what events are happening
            # print(event)
            quit_game(event)

            # responsible for checking if the snake is colliding with itself or a wall or a fruit
            game_over, snake_id = snake_screen_update(event, [snake_1, snake_2],
                                                      fruits, speed_power, slow_power)
            # updates the wall size variable
            wall_update(event, wall)
            # sets the flag to show the speed power up
            if (len(speed_power) < max_speed):
                speed_power += spawn_speed_power(event)
            # sets the flag to show the slow power up
            if (len(slow_power) < max_slow):
                slow_power += spawn_slow_power(event)
            # moves snake_1 with the arrow keys (blue snek)
            arrow_move(event, snake_1, fruits)
            # print(snake_1.get_snake_moved())
            # moves snake_2 with the W/A/S/D keys
            arrow_move(event,
                       snake_2,
                       fruits,
                       up=pygame.K_w,
                       down=pygame.K_s,
                       left=pygame.K_a,
                       right=pygame.K_d)
        if game_over == True:

            print("game ended")
            return snake_id

        # gives the scale surface a color (from global_values.py)
        rect = game_surface.get_rect(
            center=(screen.get_width()/2, screen.get_height()/2))
        sidebar_length = (screen.get_width() - border_surface.get_width())/2
        scale_surface.fill(screen_color)
        title_rect = game_title_icon.get_rect(
            center=(sidebar_length/2, (screen.get_height()/30)))
        scale_surface.blit(
            game_title_icon, title_rect)
        scale_surface.blit(yellow_snake_icon, (sidebar_length/2-10,
                           (screen.get_height()/2 + screen.get_height()/3)-30))
        scale_surface.blit(blue_snake_icon, (sidebar_length + (border_surface.get_width() +
                           (sidebar_length/2)-10), (screen.get_height()/2 + screen.get_height()/3)-30))
        scale_surface.blit(
            blue_snake_text, (sidebar_length/2, screen.get_height()/2 + screen.get_height()/3))
        scale_surface.blit(yellow_snake_text, (sidebar_length + border_surface.get_width() +
                           (sidebar_length/2), screen.get_height()/2 + screen.get_height()/3))

        border_surface.fill(border_color)
        # fills the (snake game) surface with a color (from global_values.py)

        game_surface.fill(board_color)
        for row in range(CELL_NUMBER):
            if row % 2 == 0:
                for col in range(CELL_NUMBER):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col*CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(game_surface, grass_color, grass_rect)
            else:
                for col in range(CELL_NUMBER):
                    if col % 2 == 1:
                        grass_rect = pygame.Rect(
                            col*CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pygame.draw.rect(game_surface, grass_color, grass_rect)
        # draws the snakes onto the game_surface
        snake_1.draw_elements(game_surface)
        snake_2.draw_elements(game_surface)
        # draws the fruits to the game_surface
        for i in fruits:
            i.draw_elements(game_surface)
        for i in speed_power:
            i.draw_elements(game_surface)
        for i in slow_power:
            i.draw_elements(game_surface)
        # draws the speed_power to the game_surface
        # draws the walls to the game_surface
        wall.update(game_surface)
        # blits (puts on top of) the game_surface to the scale surface in the
        # position of the rectangle made at the beginning of the loop (basically the center)
        border_surface.blit(
            game_surface, (BORDER_THICKNESS/2, BORDER_THICKNESS/2))
        scale_surface.blit(border_surface, rect)
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


pygame.init()
# Creates the main screen with the amount of cells and the size of them
screen = pygame.display.set_mode(
    (CELL_NUMBER * (CELL_SIZE+16), CELL_NUMBER * (CELL_SIZE+1)), pygame.RESIZABLE)
pygame.display.set_caption("Pythons")
pygame.display.set_icon(pygame.image.load(
    "Assets/ICON.png").convert_alpha())
while True:
    result = main(screen)
    time.sleep(0.5)
    if result == 0:
        score.set_blue_score(score.get_blue_score()+1)
    if result == 1:
        score.set_yellow_score(score.get_yellow_score()+1)
    print(f"yellow: {score.get_blue_score()}")
    print(f"blue: {score.get_yellow_score()}")
