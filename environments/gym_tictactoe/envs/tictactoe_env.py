import numpy as np
import gym
from gym import spaces

from gym_tictactoe.envs.TicTacToe import TicTacToe


BOARD_SIZE = 3


class TicTacToeEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self):
    self.tictactoe = TicTacToe(BOARD_SIZE)
    self.action_space = spaces.MultiDiscrete([BOARD_SIZE , BOARD_SIZE])
    self.observation_space = spaces.Box(low=-1, high=1, shape=[BOARD_SIZE, BOARD_SIZE], dtype=np.int32)

  def seed(self, seed=None):
    return self.tictactoe.seed(seed)

  def step(self, action):
    return self.tictactoe.step(tuple(action))

  def reset(self):
    return self.tictactoe.reset()

  def render(self, mode='human'):
    return self.tictactoe.render(mode)

  def close(self):
    return self.tictactoe.close()
