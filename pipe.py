import pygame
import sys

# Settings
square_side = 10
fps = 10
clock = pygame.time.Clock()


class Pipe(pygame.sprite.Group):
    def __init__(self, start, end, grid):
        pygame.sprite.Group.__init__(self)
        self.start = start
        self.front = self.start
        self.end = end
        self.ix = 0
        self.iy = 0
        self.add_square(self.start, grid)
        self.add_square(self.end, grid)

    def add_square(self, location, grid):
        global square_side
        #x = location[0]  #int(input('enter x value'))
        #y = location[1]  #int(input('enter x value'))
        new_square = grid[location]  #x, y, square_side)  # change to add existing square
        self.add(new_square)
        new_square.is_occupied = True
        #print(f'new sprite created at {x}, {y}')

    def update(self, game_window, grid):
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_DOWN]:
            new_y = self.front[1] + 1
            new_x = self.front[0]
            self.front = (new_x, new_y)
            self.add_square((new_x, new_y), grid)
            #TODO: Add no consuming preoccupied squares
        if key_state[pygame.K_UP]:
            new_y = self.front[1] - 1
            new_x = self.front[0]
            self.front = (new_x, new_y)
            self.add_square((new_x, new_y), grid)
        if key_state[pygame.K_LEFT]:
            new_y = self.front[1]
            new_x = self.front[0] - 1
            self.front = (new_x, new_y)
            self.add_square((new_x, new_y), grid)
        if key_state[pygame.K_RIGHT]:
            new_y = self.front[1]
            new_x = self.front[0] + 1
            self.front = (new_x, new_y)
            self.add_square((new_x, new_y), grid)
        #self.squares.update()
        if self.front == self.end:
            print('you win!!')
            sys.exit()
        self.draw(game_window)
        print('ran pipe update')