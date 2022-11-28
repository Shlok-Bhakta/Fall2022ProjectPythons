import pygame
from pygame.math import Vector2
import sys
from global_values import *


def quit_game(event):
    """checks to see if the x button is pressed then gracefully shuts down the program

    Args:
        event (event): the event to check
    """
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def snake_screen_update(event, snake=[], fruit=[]):
    """Moves the snake on the update of the screen

    Args:
        event (event): the event to check
        snake (SNAKE): the snake body
    """
    global snake_pos
    global fruit_pos
    if event.type == SCREEN_UPDATE:
        for i in snake:
            i.update()
        snake_pos = []
        fruit_pos = []
        for i in snake:
            snake_pos.append(i.get_snake_positions())

        for i in fruit:
            fruit_pos.append(i.get_fruit_positions())
        # print(f"Snake Positions {snake_pos}")
        # print(f"Fruit Positions {fruit_pos}")
        # print("\n###########################################################")
        for i in range(len(fruit_pos)):
            for j in range(len(snake)):
                if fruit_pos[i] == snake_pos[j][0]:
                    snake[j].add_block()
                    fruit[i].randomize_fruit(snake_pos, fruit_pos)


def arrow_move(event, snake, up=pygame.K_UP, down=pygame.K_DOWN, left=pygame.K_LEFT, right=pygame.K_RIGHT):
    """does movement for the snake

    Args:
        event (_type_): _description_
        snake (_type_): _description_
        up (_type_, optional): what button to press to go up. Defaults to pygame.K_UP.
        down (_type_, optional): what button to press to go down. Defaults to pygame.K_DOWN.
        left (_type_, optional): what button to press to go left. Defaults to pygame.K_LEFT.
        right (_type_, optional): what button to press to go right. Defaults to pygame.K_RIGHT.
    """
    if event.type == pygame.KEYDOWN:
        if (snake.moved == True):
            if event.key == down and snake.previous_direction != UP_VALUE:
                snake.direction = DOWN_VECTOR
                snake.previous_direction = DOWN_VALUE
                snake.moved = False
            elif event.key == up and snake.previous_direction != DOWN_VALUE:
                snake.direction = UP_VECTOR
                snake.previous_direction = UP_VALUE
                snake.moved = False
            elif event.key == left and snake.previous_direction != RIGHT_VALUE:
                snake.direction = LEFT_VECTOR
                snake.previous_direction = LEFT_VALUE
                snake.moved = False
            elif event.key == right and snake.previous_direction != LEFT_VALUE:
                snake.direction = RIGHT_VECTOR
                snake.previous_direction = RIGHT_VALUE
                snake.moved = False
    # self clipping prevention (20% success for some reason)
    if snake.start_direction == DOWN_VALUE and snake.previous_direction == UP_VALUE:
        print("SELF CLIPPING")
        snake.direction = RIGHT_VECTOR
    elif snake.start_direction == UP_VALUE and snake.previous_direction == DOWN_VALUE:
        print("SELF CLIPPING")
        snake.direction = LEFT_VECTOR
    elif snake.start_direction == LEFT_VALUE and snake.previous_direction == RIGHT_VALUE:
        print("SELF CLIPPING")
        snake.direction = DOWN_VECTOR
    elif snake.start_direction == RIGHT_VALUE and snake.previous_direction == LEFT_VALUE:
        print("SELF CLIPPING")
        snake.direction = UP_VECTOR


def window_resize(event, screen):
    """attempt to make the game have a resizable window
        doesn't work btw :)
    Args:
        event (_type_): the event to check
        screen (_type_): the screen/surface to resize

    Returns:
        _type_: _description_
    """
    cell_size = 0
    if event.type == pygame.VIDEORESIZE:
        print("resized")
        print(f"Width: {screen.get_width()}\nHeight:{screen.get_height()}")
        while screen.get_width() > CELL_NUMBER * cell_size:
            cell_size += 1

        while screen.get_height() > CELL_NUMBER * cell_size:
            print("HEIGHT OVERFLOW")
            cell_size += 1

        return int(cell_size - 1)
