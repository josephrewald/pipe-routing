import pygame
import sys
import time

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
        end_square = grid[end]
        self.add(end_square)
        print('from __init__: self.start = ', self.start)
        print('from __init__: self.end = ', self.end)

    def add_square(self, location, grid):
        #x = location[0]  #int(input('enter x value'))
        #y = location[1]  #int(input('enter x value'))
        new_square = grid[location]
        #print('from add_square: location = ', location)
        if new_square.is_occupied:
            print('Square already occupied, choose another path.')
            time.sleep(0.1)
        else:
            self.add(new_square)
        #    print('entering else', ' - ', location)
            self.front = location
            new_square.is_occupied = True
        #print(f'new sprite created at {x}, {y}')

# TODO: Check the logic of this section in conjunction with the add_square logic.
    def update(self, game_window, grid):
        print(f'running pipe.update {self.start} - {self.end}')
        key_state = pygame.key.get_pressed()
        if key_state[pygame.K_j]:
            new_y = self.front[1] + 1
            new_x = self.front[0]
            if grid[(new_x, new_y)].is_occupied:
                print('Square already occupied, choose another path.')
                time.sleep(5)
            else:
                #self.front = (new_x, new_y)
                self.add_square((new_x, new_y), grid)
            #TODO: Add no consuming preoccupied squares
        if key_state[pygame.K_k]:
            new_y = self.front[1] - 1
            new_x = self.front[0]
            #self.front = (new_x, new_y)
            self.add_square((new_x, new_y), grid)
        if key_state[pygame.K_h]:
            new_y = self.front[1]
            new_x = self.front[0] - 1
            #self.front = (new_x, new_y)
            self.add_square((new_x, new_y), grid)
        if key_state[pygame.K_l]:
            new_y = self.front[1]
            new_x = self.front[0] + 1
            #self.front = (new_x, new_y)
            self.add_square((new_x, new_y), grid)
        #self.squares.update()
        print(f'running pipe.update {self.start} - {self.end}')
        if self.front == self.end:
            print(f'front of pipe is {self.front}')
            print(f'end of pipe is {self.end}')
            print('you win!!')
            sys.exit()
        self.draw(game_window)
