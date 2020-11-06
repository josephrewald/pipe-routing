import pygame
import random
import sys

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


# Sprites
class Square(pygame.sprite.Sprite):
    #TODO: Square needs x and y grid positions, not only pixel values. The x and y grid positions
    #can be used as indices so I can access things sequentially.
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size_x = 10
        self.size_y = 10
        self.image = pygame.Surface((self.size_x, self.size_y))
        self.image.fill(color_black)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.is_occupied = False

    def update(self):
        self.image = pygame.Surface((self.size_x, self.size_y))
        if self.is_occupied:
            self.image.fill(color_white)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, start, end):
        pygame.sprite.Sprite.__init__(self)
        self.start = start
        self.end = end
        self.squares = pygame.sprite.Group()

    def add_square(self):
        global window_width
        global window_height
        x = random.randint(0, window_width)
        y = random.randint(0, window_height)
        new_square = Square(x, y)
        self.squares.add(new_square)
        new_square.is_occupied = True
        print(f'new sprite created at {x}, {y}')

    def update(self):
        # Movement
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.add_square()
        if keystate[pygame.K_LEFT]:
            self.add_square()
        if keystate[pygame.K_RIGHT]:
            self.add_square()
        self.squares.update()


def initialise_squares(window_width, window_height, square_side):
    x = 0
    y = 0
    all_squares = {}
    while x < window_width:
        while y < window_height:
            new_square = Square(x, y)
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
    grid = initialise_squares(window_width, window_height, square_side)

    pipe = Pipe((1, 2), (3, 4))

    # Game Loop
    while True:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # all_sprites.update()
        pipe.update()

        game_window.fill(color_black)
        pipe.squares.draw(game_window)
        pygame.display.flip()


if __name__ == '__main__':
    main()