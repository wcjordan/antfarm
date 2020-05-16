"""
Runner which trains a QLearning agent to play tictactoe
"""
import sys

import gym

from algorithms.q_learning import QLearning
from connectors.rest_connector import RestConnector

BASE_URI = 'http://server:8000/api/training/'


def run_tictactoe(output_connector, run_id, episodes=50, seed=None):
    """
    Train a QLearning agent using a OpenAI gym for tictactoe
    """
    env = gym.make('gym_tictactoe:tictactoe-v0')
    env.reset()
    if seed is not None:
        env.seed(seed)

    # Run Q-learning algorithm
    output_connector.begin_training_run(run_id)
    learning = QLearning(env, output_connector, seed)
    learning.train(episodes)
    env.close()
    output_connector.end_training_run(run_id)


if __name__ == '__main__':
    # Create a connector to record training data
    RUN_ID = sys.argv[1]
    CONNECTOR = RestConnector(BASE_URI, 'training_runs', 'episodes', 'steps')

    run_tictactoe(CONNECTOR, RUN_ID)
