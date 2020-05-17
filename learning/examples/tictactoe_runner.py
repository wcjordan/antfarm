"""
Simple example which plays tictactoe randomly
Doesn't use any learning agent or OpenAI gym
"""
import random

from gym_tictactoe.envs.TicTacToe import TicTacToe


def run():
    """
    Play a single game
    """
    env = TicTacToe(3)
    reward = 0
    done = False
    env.reset()
    while not done:
        actions = env.action_space

        chosen_action = _choose_action(actions)
        print(chosen_action)
        _, reward, done, _ = env.step(chosen_action)
        if reward != -0.3:
            env.render()

    if reward == 1:
        print('You Win!!!!!')
    elif reward == -1:
        print('You Lose :(')
    else:
        print('Cats Game :/')


# Random Agent
# See q_learning_tictactoe for a reinforcement learning example
def _choose_action(actions):
    return random.choice(actions)


if __name__ == "__main__":
    run()
