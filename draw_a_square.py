import pygame
import sys
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

def main():
    # Sprite Groups
    all_sprites = pygame.sprite.Group()

    my_square = Square(0, 0, 10)
    all_sprites.add(my_square)
    game_window.fill(color_black)
    while True:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        all_sprites.update()
        #pipe.update(game_window)

        #game_window.fill(color_black)
        all_sprites.draw(game_window)
        pygame.display.flip()


if __name__ == '__main__':
    main()