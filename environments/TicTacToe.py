import copy
import random

EMPTY_SQ = ''
USER_PLAYER = 'X'
AI_PLAYER = 'O'

class TicTacToe:
    ''' TODO Handle cats game outcome when working on runner
    Available spaces will be empty
    '''

    def __init__(self, board_size):
        self.board_size = board_size
        self.board = [[EMPTY_SQ]*self.board_size for row in range(board_size)]
        self.available_spaces = self._init_available_spaces()
        self.win_lines = self._init_win_lines()
        self.outcome = EMPTY_SQ

    def list_actions(self):
        ''' Returns a list of available actions
        '''
        if self._get_outcome() != EMPTY_SQ:
            return []
        return self._get_available_spaces()

    def take_action(self, action):
        ''' Updates state w/ action
        Returns a reward and observation
        '''
        self._apply_action(action, USER_PLAYER)
        outcome = self._get_outcome()
        if outcome == EMPTY_SQ:
            self._play_ai()

        outcome = self._get_outcome()
        reward = 0
        if (outcome == USER_PLAYER):
            reward = 1
        elif (outcome == AI_PLAYER):
            reward = -1

        return reward, copy.deepcopy(self.board);

    def _get_outcome(self):
        return self.outcome

    def _get_available_spaces(self):
        return self.available_spaces

    def _init_win_lines(self):
        winning_cols = [[(row, col) for row in range(self.board_size)] for col in range(self.board_size)]
        winning_rows = [[(row, col) for col in range(self.board_size)] for row in range(self.board_size)]
        forward_diagonal = [(pos, pos) for pos in range(self.board_size)]
        back_diagonal = [(self.board_size - pos - 1, pos) for pos in range(self.board_size)]
        return winning_cols + winning_rows + [forward_diagonal, back_diagonal]

    def _init_available_spaces(self):
        return [(row, col) for row in range(self.board_size) for col in range(self.board_size)]

    def _get_pos(self, pos):
        return self.board[pos[0]][pos[1]]

    def _set_pos(self, pos, value):
        self.board[pos[0]][pos[1]] = value

    def _apply_action(self, action, player):
        available_spaces = self._get_available_spaces()
        if action not in available_spaces:
            print('Space not available {}'.format(action))
            return

        available_spaces.remove(action)
        self._set_pos(action, player)

        won = any([all([self._get_pos(pos) == player for pos in line]) for line in self.win_lines])
        if won:
            self.outcome = player

    # Basic AI below
    # TODO move to another class
    def _play_ai(self):
        actions = self._get_available_spaces()
        if len(actions) == 0:
            return

        action = self._choose_action()
        self._apply_action(action, AI_PLAYER)

    def _choose_action(self):
        move = self._get_winning_or_saving_move()
        if move:
            return move

        return random.choice(self._get_available_spaces())

    def _find_empty_sq(self, line):
        for pos in line:
            if EMPTY_SQ == self._get_pos(pos):
                return pos

        raise ValueError('Expected line {} to include at least one empty square'.format(line))

    def _get_winning_or_saving_move(self):
        available_spaces = self._get_available_spaces()

        def _score_line(char):
            if char == USER_PLAYER:
                return -1
            if char == AI_PLAYER:
                return 1
            return 0

        saving_pos = None
        scores = [{ 'idx': idx, 'score': sum([_score_line(self._get_pos(pos)) for pos in line]) } for idx, line in enumerate(self.win_lines)]
        for score in scores:
            score_val = score['score']
            line = self.win_lines[score['idx']]
            if score_val == self.board_size - 1:
                return self._find_empty_sq(line)

            if saving_pos is None and score_val == -1 * (self.board_size - 1):
                saving_pos = self._find_empty_sq(line)

        return saving_pos
