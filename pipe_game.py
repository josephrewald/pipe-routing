import pygame
import sys
from pipe import Pipe
from square import Square

# ---initialise Pygame---#
pygame.init()

# Settings
window_width = 900
window_height = 600
square_side = 10
fps = 10
clock = pygame.time.Clock()
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_fuzzy = (255, 105, 180)

# ---Game Window---#
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Automating Mechanical Engineering')


def initialise_squares(window_width, window_height, square_side):
    x = 0
    y = 0
    all_squares = {}
    while x < window_width:
        while y < window_height:
            new_square = Square(x, y, square_side)
            all_squares.update({(x, y): new_square})
            x += square_side
            y += square_side
            print(f'created square at {x}, {y}')
    #while y < window_height:
    #    pass
    print(all_squares)
    return all_squares


def main():
    # Sprite Groups
    # all_sprites = pygame.sprite.Group()

    global window_width
    global window_height
    global square_side
    #grid = initialise_squares(window_width, window_height, square_side)

    pipe = Pipe((1, 2), (3, 4))

    # Game Loop
    while True:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # all_sprites.update()
        pipe.update(game_window)

        #########game_window.fill(color_black)
        #pipe.squares.draw(game_window)
        pygame.display.flip()


if __name__ == '__main__':
    main()