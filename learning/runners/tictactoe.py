import sys

import gym

from algorithms.q_learning import QLearning
from connectors.RestConnector import RestConnector

BASE_URI = 'http://server:8000/api/training/'

if __name__ == '__main__':
    env = gym.make('gym_tictactoe:tictactoe-v0')
    env.reset()

    # Create a connector to record training data
    id = sys.argv[1]
    output_connector = RestConnector(BASE_URI, 'training_runs', 'episodes',
                                     'steps')
    output_connector.begin_training_run(
        id)  # 'TicTacToe - QLearning - {}'.format(str(uuid.uuid4()))

    # Run Q-learning algorithm
    QLearning(env, output_connector, 0.2, 0.9, 0.8, 0, 500)
    env.close()
    output_connector.end_training_run(id)
