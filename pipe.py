import pygame
import sys
import time

class Pipe(pygame.sprite.Group):
    def __init__(self, start, end, grid):
        pygame.sprite.Group.__init__(self)
        self.start = start
        self.front = self.start
        self.end = end
        self.ix = 0
        self.iy = 0
        self.add_square(self.start, grid)
        end_square = grid[end]
        self.add(end_square)
        self.done = False
        self.illegal_moves = 0

    def add_square(self, location, grid):
        new_square = grid[location]
        if new_square.is_occupied:
            print('Square already occupied, choose another path.')
            time.sleep(0.1)
            self.illegal_moves += 1
        else:
            self.add(new_square)
            self.front = location
            new_square.is_occupied = True

    def update(self, game_window, grid):
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_j]:
            new_y = self.front[1] + 1
            new_x = self.front[0]
            self.add_square((new_x, new_y), grid)
        if key_state[pygame.K_k]:
            new_y = self.front[1] - 1
            new_x = self.front[0]
            self.add_square((new_x, new_y), grid)
        if key_state[pygame.K_h]:
            new_y = self.front[1]
            new_x = self.front[0] - 1
            self.add_square((new_x, new_y), grid)
        if key_state[pygame.K_l]:
            new_y = self.front[1]
            new_x = self.front[0] + 1
            self.add_square((new_x, new_y), grid)
        if self.front == self.end:
            print('you win!!')
            self.done = True
            #sys.exit()
        self.draw(game_window)
