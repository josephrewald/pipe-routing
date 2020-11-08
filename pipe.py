import pygame
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
        self.ix = 0
        self.iy = 0

    def add_square(self, x, y):
        global window_width
        global window_height
        global square_side
        new_square = Square(x, y, square_side)
        self.add(new_square)
        new_square.is_occupied = True
        print(f'new sprite created at {x}, {y}')

    def update(self, game_window):
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_UP]:
            self.add_square(self.ix, self.iy)
            self.ix += 1
            self.iy += 1
        #if key_state[pygame.K_LEFT]:
        #    self.add_square()
        #if key_state[pygame.K_RIGHT]:
        #    self.add_square()
        #self.squares.update()
        self.draw(game_window)
        print('ran pipe update')