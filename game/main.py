import pygame
import sys
from pipe import Pipe
from square import Square
from wall import Wall
from mygame import MyGame


# Settings
window_width = 900
window_height = 600
square_side = 10
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_fuzzy = (255, 105, 180)

if __name__ == "__main__":
    game = MyGame(window_width, window_height, square_side)
    length, fuck_ups = game.episode()
    G = -(length + fuck_ups)
    print(length, fuck_ups)
