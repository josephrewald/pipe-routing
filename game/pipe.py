import pygame
import sys
import time

class Pipe(pygame.sprite.Group):
    def __init__(self, start, end, grid, agent, policy_net):
        pygame.sprite.Group.__init__(self)
        self.start = start
        self.front = self.start
        self.end = end
        self.grid = grid
        self.ix = 0
        self.iy = 0
        self.add_square(self.start)
        end_square = self.grid[end]
        self.add(end_square)
        self.done = False
        self.illegal_moves = 0
        self.agent = agent
        self.policy_net = policy_net

    def add_square(self, location):
        new_square = self.grid[location]
        if new_square.is_occupied:
            print('Square already occupied, choose another path.')
            #time.sleep(0.1)
            self.illegal_moves += 1
        else:
            self.add(new_square)
            self.front = location
            new_square.is_occupied = True
        return self.get_state()

    def get_state(self):
        state = self.grid.update_state()
        front_x = self.front[0]
        front_y = self.front[1]
        state[front_x][front_y] += 1
        return state

    def update(self, game_window, new_state):
        #key_state = pygame.key.get_pressed()
        current_state = self.get_state()
        action = self.agent.select_action(current_state, self.policy_net)
        square_down = (self.front[0], self.front[1] + 1)
        square_up = (self.front[0], self.front[1] - 1)
        square_left = (self.front[0] - 1, self.front[1])
        square_right = (self.front[0] + 1, self.front[1])
        stuck = self.grid[square_down].is_occupied and \
                self.grid[square_left].is_occupied and \
                self.grid[square_right].is_occupied and \
                self.grid[square_up].is_occupied 
        if stuck:
            print("you lose")
            self.illegal_moves += 100
            self.done = True
        if action == 0: #key_state[pygame.K_j]: # DOWN
            #new_y = self.front[1] + 1
            #new_x = self.front[0]
            new_state = self.add_square(square_down)
        if action == 1: #key_state[pygame.K_k]: # UP
            #new_y = self.front[1] - 1
            #new_x = self.front[0]
            new_state = self.add_square(square_up)
        if action == 2: #key_state[pygame.K_h]: # LEFT
            #new_y = self.front[1]
            #new_x = self.front[0] - 1
            new_state = self.add_square(square_left)
        if action == 3: #key_state[pygame.K_l]: # RIGHT
            #new_y = self.front[1]
            #new_x = self.front[0] + 1
            new_state = self.add_square(square_right)
        if self.front == self.end:
            print('you win!!')
            self.done = True
            #sys.exit()
        self.draw(game_window)
        return new_state
