import variables
import pixel

def create():
    return Snake()

class Snake:
    def __init__(self):
        middle_x = int(variables.SCREEN_WIDTH / 2)
        middle_y = int(variables.SCREEN_HEIGHT / 2)

        # Body of the snake is an array of Pixels
        # Head is the first element
        # Always initialized to the middle of the screen
        self.body = [pixel.create(variables.SNAKE_COLOR, x=middle_x, y=middle_y)]

        # "UP", "DOWN", "LEFT", "RIGHT".
        self.moving_direction = variables.DEFAULT_SNAKE_MOVING_DIRECTION

    def head(self):
        return self.body[0]
    
    def tail(self):
        return self.body[-1]
    
    def size(self):
        return len(self.body)
    
    def check_body_collision(self):
        all_pixels = set()
        for pixel in self.body:
            all_pixels.add((pixel.x, pixel.y))

        return len(all_pixels) != self.size()
    
    def increase_snake_size(self):
        x, y = self.tail().x, self.tail().y
        parent_direction = self.get_parent_direction()
        mov_x, mov_y = 0, 0
        
        # place below tail
        if parent_direction == "UP":
            mov_y = variables.PIXEL_HEIGHT
        # place above tail
        if parent_direction == "DOWN":
            mov_y = -variables.PIXEL_HEIGHT
        # place left tail
        if parent_direction == "RIGHT":
            mov_x = -variables.PIXEL_WIDTH
        if parent_direction == "LEFT":
            mov_x = variables.PIXEL_WIDTH

        new_tail = pixel.create(variables.SNAKE_COLOR, x = x + mov_x, y = y + mov_y)
        self.body.append(new_tail)
        
    def get_parent_direction(self):
        if (self.size() == 1):
            return self.moving_direction
        
        tail = self.tail()
        tail_parent = self.body[-1]
        is_up = tail_parent.y > tail.y
        is_down = tail_parent.y < tail.y
        is_right = tail_parent.x > tail.x
        is_left = tail_parent.x < tail.x
        if is_up: return "UP"
        if is_down: return "DOWN"
        if is_right: return "RIGHT"
        if is_left: return "LEFT"

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
        for i in range(self.size() - 1, 0, - 1):
            current_pixel = self.body[i]
            next_pixel = self.body[i - 1]
            current_pixel.move_to(next_pixel.x, next_pixel.y)

        # update head
        self.head().x += mov_x
        self.head().y += mov_y

    def draw(self, screen):
        for pixel in self.body:
            pixel.draw(screen)