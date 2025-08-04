import pygame
import variables
import fruit
import snake
import utils

pygame.init()

screen = pygame.display.set_mode((variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(variables.TITLE)
game_snake = snake.create()
game_fruit = fruit.create(game_snake)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_pressed = utils.get_key_pressed()
    if key_pressed:
        game_snake.moving_direction = key_pressed

    body_collision = game_snake.check_body_collision()
    if body_collision:
        running = False

    fruit_eaten = utils.check_fruit_eaten(game_snake.head(), game_fruit)
    if fruit_eaten:
        game_snake.increase_snake_size()
        game_fruit = fruit.create(game_snake)

    screen.fill("black")

    game_fruit.draw(screen)
    game_snake.draw(screen)

    pygame.display.flip()

    clock.tick(variables.FPS)

pygame.quit()