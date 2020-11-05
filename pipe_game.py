import pygame, sys, random

#---initialise Pygame---#
pygame.init()

#Settings
window_width = 900
window_height = 600
square_side = 10
fps = 10
clock = pygame.time.Clock()
color_white = (255,255,255)
color_black = (0, 0, 0)
color_fuzzy = (255, 105, 180)

#---Game Window---#
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Automating Menchanical Engineering')

#Sprites
class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.size_x = 10
        self.size_y = 10
        self.image = pygame.Surface((self.size_x, self.size_y))
        self.image.fill(color_white)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.is_occupied = False

    def update(self):
        self.dy = 0

        #Movement
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            #self.size_y += 10
            pass
        if keystate[pygame.K_DOWN]:
            #self.size_x += 10
            pass
        self.rect.y += self.dy
        self.image = pygame.Surface((self.size_x, self.size_y))
        self.image.fill(color_white)

class Pipe(): #TODO Make this class a sprite group..? 
    def __init__(self, start, end):
        pygame.sprite.Sprite.__init__(self)
        self.start = start
        self.end = end
        self.squares = []
        self.my_sprites = pygame.sprite.Group()

    def add_square(self):
        global window_width
        global window_height
        x = random.randint(0, window_width)
        y = random.randint(0, window_height)
        new_square = Square(x, y)
        self.squares.append(new_square)
        self.my_sprites.add(new_square)
        print(f'new sprite created at {x}, {y}')

    def update(self):
        #Movement
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            #print('from update: self.squares is a ', type(self.squares))
            #self.squares.append(square)
            self.add_square()
        self.my_sprites.update()
        #self.my_sprites.draw(game_window)
        #self.squares.draw(game_window)

def main():

    #Sprite Groups
    #all_sprites = pygame.sprite.Group()
    
    square = Square(25, 0)
    anothersquare = Square(100, 0)
    pipe = Pipe((1,2), (3, 4))
    #all_sprites.add(square, anothersquare)
    
    #Game Loop
    while True:
        #Set framerate
        clock.tick(fps)
    
        #Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        #update
        #all_sprites.update()
        pipe.update()
    
        #draw
            #Fill
        game_window.fill(color_black)
            #Sprites
        #all_sprites.draw(game_window)
        pipe.my_sprites.draw(game_window)
    
    
        #flip
        pygame.display.flip()
    
    pygame.quit()

if __name__ == '__main__':
    main()
