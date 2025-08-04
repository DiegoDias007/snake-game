import pygame
import pixel
import variables
import snake
import utils

pygame.init()

screen = pygame.display.set_mode((variables.SCREEN_WIDTH, variables.SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(variables.TITLE)
fruit = pixel.create(variables.FRUIT_COLOR)
snake = snake.create()

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    key_pressed = utils.get_key_pressed()
    if key_pressed:
        snake.moving_direction = key_pressed

    body_collision = snake.check_body_collision()
    if body_collision:
        running = False

    fruit_eaten = utils.check_fruit_eaten(snake.head(), fruit)
    if fruit_eaten:
        snake.increase_snake_size()
        # update fruit position

    screen.fill("black")

    fruit.draw(screen)
    snake.draw(screen)

    pygame.display.flip()

    clock.tick(variables.FPS)

pygame.quit()