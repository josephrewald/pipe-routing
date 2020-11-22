import pygame

# Settings
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_fuzzy = (255, 105, 180)


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, side):  # x, y are indices
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.Surface((side, side))
        self.image.fill(color_white)
        self.rect = self.image.get_rect()
        self.rect.left = x * side
        self.rect.top = y * side
        self.is_occupied = False

    def update(self):
        #self.image = pygame.Surface((self.x, self.y))
        if self.is_occupied:
            self.image.fill(color_white)
            print('ran square update')