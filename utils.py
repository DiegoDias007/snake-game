import random
import variables

def get_random_coordinates():
    width_limit = variables.SCREEN_WIDTH - variables.PIXEL_WIDTH
    height_limit = variables.SCREEN_HEIGHT - variables.PIXEL_HEIGHT
    x = random.randint(0, width_limit)
    y = random.randint(0, height_limit)
    return x, y