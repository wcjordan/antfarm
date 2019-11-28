import random

from environments.TicTacToe import TicTacToe


def run():
    game = TicTacToe(3)
    reward = 0
    while True:
        actions = game.list_actions()
        if len(actions) == 0:
            break

        chosen_action = _choose_action(actions)
        print(chosen_action)
        reward, board = game.take_action(chosen_action)
        _render_board(board)

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


# Render board
# TODO move to seperate render method
def _render_board(board):
    for row in board:
        print('', end=' | ')
        for sq in row:
            print(sq or ' ', end=' | ')
        print('')
    print('\n')


if __name__ == "__main__":
    run()
