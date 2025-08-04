import utils
import pixel
import variables

def create(snake):
    x, y = utils.get_safe_fruit_coordinates(snake)
    return pixel.create(variables.FRUIT_COLOR, x, y)