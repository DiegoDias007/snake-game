# Snake Game!

This is a classic Snake game implemented in Python using the Pygame library.

## How to Play

The objective of the game is to control the snake and eat the red fruit to grow longer. The game ends if the snake collides with itself or hits the screen's boundaries.

### Controls

* **Up**: `W` or `Up Arrow`
* **Down**: `S` or `Down Arrow`
* **Left**: `A` or `Left Arrow`
* **Right**: `D` or `Right Arrow`

## Game Features

* **Dynamic Snake Movement**: The snake moves in one of four directions: up, down, left, or right. The player controls the direction of the snake's head.
* **Fruit Generation**: A red fruit appears at random coordinates on the screen. The fruit is always placed in a position that is not occupied by the snake's body.
* **Collision Detection**: The game ends if the snake's head collides with any part of its body or goes out of the screen boundaries.
* **Scoring**: Eating a fruit increases the snake's size.

## How to Run

1.  **Prerequisites**: Make sure you have Python and Pygame installed. If not, you can install Pygame using pip:
    ```bash
    pip install pygame
    ```

2.  **Run the game**: Navigate to the directory containing the game files and run the `main.py` file:
    ```bash
    python main.py
    ```