import pygame
import variables
import utils

def create(color, x=None, y=None):
    if x == None or y == None:
        x, y = utils.get_random_coordinates()

    return Pixel(x, y, variables.PIXEL_WIDTH, variables.PIXEL_HEIGHT, color)

class Pixel:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))