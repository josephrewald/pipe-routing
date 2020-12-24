import pygame
import sys
from pipe import Pipe
from square import Square
from wall import Wall
from main_loop import MainLoop

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
    main_loop = MainLoop(window_width, window_height, square_side)
    length = main_loop.episode()
    print(length)
