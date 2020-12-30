import pygame
import sys

import torch
import torch.optim as optim

from game.pipe import Pipe
from game.square import Square
from game.wall import Wall
from game.mygame import MyGame
from game.grid import Grid

from AI.agent import Agent
from AI.dqn import DQN
#from AI.env_manager import CartPoleEnvManager
from AI.epsilon_greedy_strategy import EpsilonGreedyStrategy
from AI.experience import Experience
from AI.q_values import QValues
from AI.replay_memory import ReplayMemory
from AI.utils import plot, get_moving_average, extract_tensors
from AI.training_function import training_function


# Settings
window_width = 100
window_height = 100
square_side = 10
color_white = (255, 255, 255)
color_black = (0, 0, 0)
color_fuzzy = (255, 105, 180)

batch_size =    128 # 256 - number of replay memory experiences considered
gamma =         0.9 # 0.999 - discount factor in Bellman eqn
eps_start =     1 # 1 - exploration rate
eps_end =       0.01 # 0.01
eps_decay =     0.01 # 0.001
target_update = 10 # 10 - frequency for updating target network
memory_size =   100000 # 100000 - capacity of replay memory
lr =            0.001 # 0.001 - learning rate
num_episodes =  1000 # 1000
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")



if __name__ == "__main__":
    strategy = EpsilonGreedyStrategy(eps_start, eps_end, eps_decay)
    agent = Agent(strategy, 4, device)
    memory = ReplayMemory(memory_size)
    grid = Grid(window_width, window_height, square_side)
    policy_net = DQN(grid.size_x, grid.size_y).to(device)
    target_net = DQN(grid.size_x, grid.size_y).to(device)
    target_net.load_state_dict(policy_net.state_dict())
    target_net.eval()
    optimizer = optim.Adam(params=policy_net.parameters(), lr=lr)
    
    episode_scores = []
    for _ in range(num_episodes):
        grid = Grid(window_width, window_height, square_side)
        game = MyGame(window_width, window_height, square_side, agent, policy_net, grid)
        length, fuck_ups = game.episode()
        score = -(length + fuck_ups)
        episode_scores.append(score)
