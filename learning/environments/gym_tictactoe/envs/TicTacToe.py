import copy
import random
import sys

EMPTY_SQ = 0
USER_PLAYER = 1
AI_PLAYER = -1
DISPLAY_MAPPING = ('0', ' ', 'X')


class TicTacToe:
    '''TODO observation_space & reward_range for open AI gym
    '''

    def __init__(self, board_size):
        self._seed = random.randrange(sys.maxsize)
        random.seed(self._seed)

        self.board_size = board_size
        self.win_lines = self._init_win_lines()
        self.reset()

    def reset(self):
        self.board = [
            [EMPTY_SQ] * self.board_size for row in range(self.board_size)
        ]
        self.all_spaces = self._init_available_spaces()
        self.available_spaces = copy.deepcopy(self.all_spaces)
        self.outcome = EMPTY_SQ
        return copy.deepcopy(self.board)

    def close(self):
        pass

    def seed(self, seed=None):
        if seed is not None:
            self._seed = seed
            random.seed(seed)
        return self._seed

    @property
    def action_space(self):
        ''' Returns a list of available actions
        '''
        return self.all_spaces
        # if self._get_outcome() != EMPTY_SQ:
        #     return []
        # return self._get_available_spaces()

    def step(self, action):
        ''' Updates state w/ action
        Returns a reward and observation
        '''
        available_spaces = self._get_available_spaces()
        if action not in available_spaces:
            return copy.deepcopy(self.board), -0.3, self._is_done(), {}

        self._apply_action(action, USER_PLAYER)
        outcome = self._get_outcome()
        if outcome == EMPTY_SQ:
            self._play_ai()

        outcome = self._get_outcome()
        reward = 0
        if outcome == USER_PLAYER:
            reward = 1
        elif outcome == AI_PLAYER:
            reward = -1

        return copy.deepcopy(self.board), reward, self._is_done(), {}

    def render(self, mode='human'):
        ''' TODO handle modes 'human' & 'rgb_array'
        '''
        for row in self.board:
            print('', end=' | ')
            for sq in row:
                print(DISPLAY_MAPPING[sq + 1], end=' | ')
            print('')
        print('\n')

    def _is_done(self):
        if self._get_outcome() != EMPTY_SQ:
            return True
        return len(self._get_available_spaces()) == 0

    def _get_outcome(self):
        return self.outcome

    def _get_available_spaces(self):
        return self.available_spaces

    def _init_win_lines(self):
        winning_cols = [[(row, col)
                         for row in range(self.board_size)]
                        for col in range(self.board_size)]
        winning_rows = [[(row, col)
                         for col in range(self.board_size)]
                        for row in range(self.board_size)]
        forward_diagonal = [(pos, pos) for pos in range(self.board_size)]
        back_diagonal = [
            (self.board_size - pos - 1, pos) for pos in range(self.board_size)
        ]
        return winning_cols + winning_rows + [forward_diagonal, back_diagonal]

    def _init_available_spaces(self):
        return [(row, col)
                for row in range(self.board_size)
                for col in range(self.board_size)]

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

        won = any([
            all([self._get_pos(pos) == player
                 for pos in line])
            for line in self.win_lines
        ])
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

        raise ValueError(
            'Expected line {} to include at least one empty square'.format(
                line))

    def _get_winning_or_saving_move(self):

        def _score_line(char):
            if char == USER_PLAYER:
                return -1
            if char == AI_PLAYER:
                return 1
            return 0

        saving_pos = None
        scores = [{
            'idx': idx,
            'score': sum([_score_line(self._get_pos(pos)) for pos in line])
        } for idx, line in enumerate(self.win_lines)]
        for score in scores:
            score_val = score['score']
            line = self.win_lines[score['idx']]
            if score_val == self.board_size - 1:
                return self._find_empty_sq(line)

            if saving_pos is None and score_val == -1 * (self.board_size - 1):
                saving_pos = self._find_empty_sq(line)

        return saving_pos
