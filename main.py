import pygame
import pixel
import variables
import snake

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

    screen.fill("black")

    fruit.draw(screen)
    snake.draw(screen)

    pygame.display.flip()

    clock.tick(variables.FPS)

pygame.quit()