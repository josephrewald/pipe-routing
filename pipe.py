import pygame
import random
from square import Square

# Settings
window_width = 900
window_height = 600
square_side = 10
fps = 10
clock = pygame.time.Clock()


class Pipe(pygame.sprite.Group):
    def __init__(self, start, end):
        pygame.sprite.Group.__init__(self)
        self.start = start
        self.end = end

    def add_square(self):
        global window_width
        global window_height
        x = random.randint(0, window_width)
        y = random.randint(0, window_height)
        global square_side
        new_square = Square(x, y, square_side)
        self.squares.add(new_square)
        new_square.is_occupied = True
        print(f'new sprite created at {x}, {y}')

    def update(self, game_window):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.add_square()
        if keystate[pygame.K_LEFT]:
            self.add_square()
        if keystate[pygame.K_RIGHT]:
            self.add_square()
        #self.squares.update()
        self.squares.draw(game_window)
        print('ran pipe update')