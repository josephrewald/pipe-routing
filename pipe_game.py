import pygame
import sys
from pipe import Pipe
from square import Square

# TODO: at 1000 lines, add tests, remove ugliness.
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


def initialise_squares(window_width, window_height, square_side, grid):
    x = 0
    y = 0
    while y*square_side < window_height:
        while x*square_side < window_width:
            new_square = Square(x, y, square_side)
            grid.update({(x, y): new_square})
            x += 1
            print(f'created square at {x}, {y}')
            print(new_square.is_occupied)
        x = 0
        y += 1


def main():
    # Sprite Groups
    # all_sprites = pygame.sprite.Group()

    global window_width
    global window_height
    global square_side
    grid = {}  #initialise_squares(window_width, window_height, square_side)
    initialise_squares(window_width, window_height, square_side, grid)

    pipe = Pipe((0, 0), (0, 10), grid)
    print(f'created pipe at {pipe.start}, {pipe.end}')

    # Game Loop
    # TODO: turn game loop into a function called "run()" to modularise stuff
    while True:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        print(f'Running game loop - {pipe.start}, {pipe.end}')
        # all_sprites.update()
        pipe.update(game_window, grid)

        #########game_window.fill(color_black)
        pipe.draw(game_window)
        pygame.display.flip()


if __name__ == '__main__':
    main()
