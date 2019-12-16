import random

from gym_tictactoe.envs.TicTacToe import TicTacToe


def run():
    env = TicTacToe(3)
    reward = 0
    done = False
    board = env.reset()
    while not done:
        actions = env.action_space

        chosen_action = _choose_action(actions)
        print(chosen_action)
        board, reward, done, info = env.step(chosen_action)
        if reward != -0.3:
            env.render()

    if reward == 1:
        print('You Win!!!!!')
    elif reward == -1:
        print('You Lose :(')
    else:
        print('Cats Game :/')


# Agent
# TODO replace w/ reinforcement learning
def _choose_action(actions):
    return random.choice(actions)


if __name__ == "__main__":
    run()
