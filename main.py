import pygame
import sys
from pipe import Pipe
from square import Square
from wall import Wall
from mygame import MyGame

# TODO: add initial AI: adds ~150 lines => ~300 LOC
# TODO: add multiple pipes: adds <100 lines = ~400 LOC
# TODO: add 3rd dimension by using colour: adds 100 lines => 500 LOC
# TODO: at 500 lines, add tests, remove ugliness.
# TODO: create 3D version of the game with Open Cascade
# TODO: apply AI to 3D version
# TODO: optimise AI
# Get rich!


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
