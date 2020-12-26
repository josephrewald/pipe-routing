from square import Square
import pygame

class grid(pygame.sprite.Group):
    def __init__(self, window_width, window_height, square_side):
        pygame.sprite.Group.__init__(self)

        x = 0
        y = 0
        while y * square_side < window_height:
            while x * square_side < window_width:
                new_square = Square(x, y, square_side)
                self.add(new_square)
                x += 1
                print(f"created square at {x}, {y}")
                print(new_square.is_occupied)
            x = 0
            y += 1


def initialise_squares(window_width, window_height, square_side, grid):
    x = 0
    y = 0
    while y * square_side < window_height:
        while x * square_side < window_width:
            new_square = Square(x, y, square_side)
            grid.update({(x, y): new_square})
            x += 1
            print(f"created square at {x}, {y}")
            print(new_square.is_occupied)
        x = 0
        y += 1
    #print(grid)
