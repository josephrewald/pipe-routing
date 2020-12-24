from initialise_squares import initialise_squares
from pipe import Pipe
from wall import Wall
import pygame
import sys


pygame.init()
#fps = 10
class MainLoop():
    def __init__(self, window_width, window_height, square_side, fps=10):
        self.window_width = window_width
        self.window_height = window_height
        self.square_side = square_side
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.game_window = pygame.display.set_mode((window_width, window_height))
        #self.pygame.display.set_caption("Automating Mechanical Engineering")

        self.grid = {}
        initialise_squares(self.window_width, self.window_height, \
                self.square_side, self.grid)
    
        self.pipe = Pipe((5, 5), (5, 15), self.grid)
        self.wall = Wall(self.grid)
    
    def episode(self):
        while self.pipe.done == False:
            self.clock.tick(self.fps)
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
            self.pipe.update(self.game_window, self.grid)
            self.wall.update(self.game_window, self.grid)
    
            self.pipe.draw(self.game_window)
            pygame.display.flip()

        return len(self.pipe)
