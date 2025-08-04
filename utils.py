import random
import pygame
import variables

def get_random_coordinates():
    width_limit = variables.SCREEN_WIDTH - variables.PIXEL_WIDTH
    height_limit = variables.SCREEN_HEIGHT - variables.PIXEL_HEIGHT
    x = random.randint(0, width_limit)
    y = random.randint(0, height_limit)

    # Make sure x is a multiple of pixel_width
    x_norm = x - x % variables.PIXEL_WIDTH
    # Making sure y is a multiple of pixel_height
    y_norm = y - y % variables.PIXEL_HEIGHT
    return x_norm, y_norm

def get_safe_fruit_coordinates(game_snake):
    snake_coords = set()
    for game_pixel in game_snake.body:
        snake_coords.add((game_pixel.x, game_pixel.y))

    while True:
        x, y = get_random_coordinates()
        if (x, y) in snake_coords:
            continue
        return x, y

def get_key_pressed():
    keys = pygame.key.get_pressed()
    # Left movement (A or Left Arrow)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        return "LEFT"

    # Right movement (D or Right Arrow)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        return "RIGHT"

    # Up movement (W or Up Arrow)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        return "UP"

    # Down movement (S or Down Arrow)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        return "DOWN"

    return None

def check_fruit_eaten(snake_head, game_fruit):
    match_x = snake_head.x == game_fruit.x
    match_y = snake_head.y == game_fruit.y
    return match_x and match_y

