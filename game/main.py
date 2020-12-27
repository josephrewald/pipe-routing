import pygame
import sys
from pipe import Pipe
from square import Square
from wall import Wall
from mygame import MyGame
#from pipe-routing.AI.epsilon_greedy_strategy import EpsilonGreedyStrategy


# Settings
window_width = 900
window_height = 600
square_side = 10
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_fuzzy = (255, 105, 180)

# create agent here

#em = CartPoleEnvManager(device)
#strategy = EpsilonGreedyStrategy(eps_start, eps_end, eps_decay)
#agent = Agent(strategy, em.num_actions_available(), device)
#memory = ReplayMemory(memory_size)
#policy_net = DQN(em.get_screen_height(), em.get_screen_width()).to(device)
#target_net = DQN(em.get_screen_height(), em.get_screen_width()).to(device)
#target_net.load_state_dict(policy_net.state_dict())
#target_net.eval()
#optimizer = optim.Adam(params=policy_net.parameters(), lr=lr)
#
#episode_durations = []


if __name__ == "__main__":
    game = MyGame(window_width, window_height, square_side)
    length, fuck_ups = game.episode()
    G = -(length + fuck_ups)
    print(length, fuck_ups)
