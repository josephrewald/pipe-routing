import pygame, sys, random

#---initialise Pygame---#
pygame.init()

#Settings
window_width = 900
window_height = 600
fps = 120
clock = pygame.time.Clock()
color_white = (255,255,255)
color_black = (0, 0, 0)
color_fuzzy = (255, 105, 180)


#---Game Window---#
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Automating Menchanical Engineering')

#Sprites
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.size_x = 10
        self.size_y = 10
        self.image = pygame.Surface((self.size_x, self.size_y))
        self.image.fill(color_white)
        self.rect = self.image.get_rect()
        self.rect.left = 25
        self.rect.top = 0

    def update(self):
        self.dy = 0

        #Movement
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_UP]:
            self.dy = -3
            self.size_y += 10
        if keystate[pygame.K_DOWN]:
            self.dy = 3
        self.rect.y += self.dy
        self.image = pygame.Surface((self.size_x, self.size_y))
        self.image.fill(color_white)

        #Constraints
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > window_height:
            self.rect.bottom = window_height

#Sprite Groups
all_sprites = pygame.sprite.Group()
ball_sprite = pygame.sprite.GroupSingle()

player1 = Player1()
all_sprites.add(player1)



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
    all_sprites.update()
    ball_sprite.update()

    #draw
        #Fill
    game_window.fill(color_black)
        #Field
#    pygame.draw.line(game_window, color_white, (window_width/2, 0), (window_width/2, window_height))
#    pygame.draw.circle(game_window, color_white, (window_width//2, window_height//2), 80, 1)
#    border = pygame.Rect(0, 0, window_width, window_height)
        #Sprites
    all_sprites.draw(game_window)
    ball_sprite.draw(game_window)


    #flip
    pygame.display.flip()

pygame.quit()
