import variables
import pixel

def create():
    return Snake()

class Snake:
    def __init__(self):
        middle_x = int(variables.SCREEN_WIDTH / 2)
        middle_y = int(variables.SCREEN_HEIGHT / 2)
        
        # Body of the snake is an array of Pixels
        # Head is the last element
        # Always initialized to the middle of the screen
        self.body = [pixel.create(variables.SNAKE_COLOR, x=middle_x, y=middle_y)]

        # "UP", "DOWN", "LEFT", "RIGHT".
        self.moving_direction = variables.DEFAULT_SNAKE_MOVING_DIRECTION

    def head(self):
        return self.body[-1]
    
    def size(self):
        return len(self.body)

    def move(self):
        mov_x, mov_y = 0, 0
        if self.moving_direction == "UP":
            mov_y = -variables.PIXEL_HEIGHT
        if self.moving_direction == "DOWN":
            mov_y = variables.PIXEL_HEIGHT
        if self.moving_direction == "LEFT":
            mov_x = -variables.PIXEL_WIDTH
        if self.moving_direction == "RIGHT":
            mov_x = variables.PIXEL_HEIGHT

        # update children
        for i in range(0, self.size() - 1):
            current_pixel = self.body[i]
            next_pixel = self.body[i + 1]
            current_pixel.move_to(next_pixel.x, next_pixel.y)

        # update head
        self.head().x += mov_x
        self.head().y += mov_y

    def draw(self, screen):
        self.move()
        for pixel in self.body:
            pixel.draw(screen)