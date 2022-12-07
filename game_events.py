import pygame
from pygame.math import Vector2
import sys
from global_values import *
from speed_up import *
from slow_down import *
from math import sqrt, pow


def quit_game(event):
    """checks to see if the x button is pressed then gracefully shuts down the program

    Args:
        event (event): the event to check
    """
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def snake_screen_update(event, snake=[], fruit=[], speed_power=[], slow_power=[]):
    """Moves the snake on the update of the screen

    Args:
        event (event): the event to check
        snake (SNAKE): the snake body
    """
    global snake_pos
    global fruit_pos
    if event.type == SCREEN_UPDATE:
        snake_pos = []
        fruit_pos = []
        speed_pos = []
        slow_pos = []
        for i in snake:
            snake_pos.append(i.get_snake_positions())

        for i in fruit:
            fruit_pos.append(i.get_fruit_positions())

        for i in speed_power:
            speed_pos.append(i.get_speed_power_positions())

        for i in slow_power:
            slow_pos.append(i.get_slow_power_positions())
        # print(f"speed Positions {speed_pos}")
        # print(f"slow Positions {slow_pos}")
        # print("\n###########################################################")
        # Snake collision with fruit
        for i in range(len(fruit_pos)):
            for j in range(len(snake)):
                if fruit_pos[i] == snake_pos[j][0]:
                    snake[j].add_block()
                    fruit[i].randomize_fruit(snake_pos, fruit_pos)
                    apple_eat_sound = pygame.mixer.Sound(
                        apple_eat_sfx_path)
                    apple_eat_sound.play()

        # Snake collision with Speed Powerup
        for i in range(len(speed_pos)):
            for j in range(len(snake)):
                if speed_pos[i] == snake_pos[j][0]:
                    snake[j].boost()
                    speed_power[i].randomize_speed_power(snake_pos, speed_pos)
                    pygame.mixer.Sound(powerup_sound).play()
        # Snake collision with Slow Powerup
        for i in range(len(slow_pos)):
            for j in range(len(snake)):
                if slow_pos[i] == snake_pos[j][0]:
                    for k in range(len(snake)):
                        if snake[j] != snake[k]:
                            snake[k].slow()
                            slow_power[i].randomize_slow_power(
                                snake_pos, slow_pos)
                            pygame.mixer.Sound(powerup_sound).play()

        # Snake collision with other snakes

        for k in range(len(snake)):
            other_bodies = []
            for j in range(len(snake)):
                if k != j:
                    other_bodies += snake[j].get_snake_positions()
            collision_result, snake_id = snake[k].check_snake_collision(
                other_bodies)
            if collision_result == True:

                print("game over")
                return collision_result, snake_id

        for i in snake:
            i.update()
    return False, -1


def arrow_move(event, snake, fruit, up=pygame.K_UP, down=pygame.K_DOWN, left=pygame.K_LEFT, right=pygame.K_RIGHT):
    """does movement for the snake

    Args:
        event (_type_): _description_
        snake (_type_): _description_
        up (_type_, optional): what button to press to go up. Defaults to pygame.K_UP.
        down (_type_, optional): what button to press to go down. Defaults to pygame.K_DOWN.
        left (_type_, optional): what button to press to go left. Defaults to pygame.K_LEFT.
        right (_type_, optional): what button to press to go right. Defaults to pygame.K_RIGHT.
    """
    if snake.is_ai == False:
        if event.type == pygame.KEYDOWN:
            if event.key == down and snake.previous_direction != UP_VALUE:
                snake.previous_direction = DOWN_VALUE
                snake.direction = DOWN_VECTOR

            elif event.key == up and snake.previous_direction != DOWN_VALUE:
                snake.previous_direction = UP_VALUE
                snake.direction = UP_VECTOR

            elif event.key == left and snake.previous_direction != RIGHT_VALUE:
                snake.previous_direction = LEFT_VALUE
                snake.direction = LEFT_VECTOR

            elif event.key == right and snake.previous_direction != LEFT_VALUE:
                snake.previous_direction = RIGHT_VALUE
                snake.direction = RIGHT_VECTOR
    if snake.is_ai == True:
        # move = random.randint(0, 3)
        move = 0
        headx = snake.get_head().x
        heady = snake.get_head().y
        target_fruit = fruit[0]
        for i in fruit[1:]:
            tfx = target_fruit.get_fruit_positions().x
            tfy = target_fruit.get_fruit_positions().y
            fx = i.get_fruit_positions().x
            fy = i.get_fruit_positions().y
            dist_target = sqrt(pow(tfx-headx, 2) + pow(tfy-heady, 2))
            dist_new = sqrt(pow(fx-headx, 2) + pow(fy-heady, 2))

            if dist_target > dist_new:
                target_fruit = i
        # print(target_fruit.id)
        # print(f"{target_fruit.get_fruit_positions()} {snake.get_head()}")
        targetx = target_fruit.get_fruit_positions().x
        targety = target_fruit.get_fruit_positions().y

        if move == 0:
            direction = random.randint(1, 4)
            if targetx > headx:
                direction = RIGHT_VALUE

            elif targetx < headx:
                direction = LEFT_VALUE
            else:
                if targety > heady:
                    direction = DOWN_VALUE

                elif targety < heady:
                    direction = UP_VALUE

            if direction == RIGHT_VALUE and snake.previous_direction == LEFT_VALUE:
                direction = random.randint(UP_VALUE, DOWN_VALUE)
            elif direction == LEFT_VALUE and snake.previous_direction == RIGHT_VALUE:
                direction = random.randint(UP_VALUE, DOWN_VALUE)
            elif direction == UP_VALUE and snake.previous_direction == DOWN_VALUE:
                direction = random.randint(LEFT_VALUE, RIGHT_VALUE)
            elif direction == DOWN_VALUE and snake.previous_direction == UP_VALUE:
                direction = random.randint(LEFT_VALUE, RIGHT_VALUE)
                # elif move == 1:
                #     direction = random.randint(1, 4)
                # elif move > 0:
                #     direction = random.randint(1, 4)
                #     if targety > heady:
                #         direction = DOWN_VALUE
                #         if snake.previous_direction == UP_VALUE:
                #             direction = random.randint(LEFT_VALUE, RIGHT_VALUE)
                #         else:
                #             direction = DOWN_VALUE
                #     elif targety < heady:
                #         direction = UP_VALUE
                #         if snake.previous_direction == DOWN_VALUE:
                #             direction = random.randint(LEFT_VALUE, RIGHT_VALUE)
                #         else:
                #             direction = UP_VALUE
                #     else:
                #         if targetx > headx:
                #             direction = RIGHT_VALUE
                #             if snake.previous_direction == LEFT_VALUE:
                #                 direction = random.randint(UP_VALUE, DOWN_VALUE)
                #             else:
                #                 direction = RIGHT_VALUE
                #         elif targetx < headx:
                #             direction = LEFT_VALUE
                #             if snake.previous_direction == RIGHT_VALUE:
                #                 direction = random.randint(UP_VALUE, DOWN_VALUE)
                #             else:
                #                 direction = LEFT_VALUE
                # print(direction)
            if direction == UP_VALUE and snake.previous_direction != DOWN_VALUE:
                snake.previous_direction = UP_VALUE
                snake.direction = UP_VECTOR
            elif direction == DOWN_VALUE and snake.previous_direction != UP_VALUE:
                snake.previous_direction = DOWN_VALUE
                snake.direction = DOWN_VECTOR
            elif direction == LEFT_VALUE and snake.previous_direction != RIGHT_VALUE:
                snake.previous_direction = LEFT_VALUE
                snake.direction = LEFT_VECTOR
            elif direction == RIGHT_VALUE and snake.previous_direction != LEFT_VALUE:
                snake.previous_direction = RIGHT_VALUE
                snake.direction = RIGHT_VECTOR


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


def wall_update(event, wall):
    """updates the wall to move it is

    Args:
        event (_type_): _description_
        wall (_type_): _description_
    """
    if event.type == WALL_UPDATE:
        if not (close.get_close_amount() > wall_cutoff):
            pygame.mixer.Sound(closing_sound).play()
            close_amount = close.get_close_amount() + 1
            close.set_close_amount(close_amount)
            # print(f"close_amount: {close.get_close_amount()}")
            wall.make_wall()


def spawn_speed_power(event):
    if event.type == SPEED_SPAWN:
        speed_power = []
        for i in range(1):
            speed_power.append(SPEED_POWER())
        return speed_power
    else:
        return []


def spawn_slow_power(event):
    if event.type == SLOW_SPAWN:
        slow_power = []
        for i in range(1):
            slow_power.append(SLOW_POWER())
        return slow_power
    else:
        return []
