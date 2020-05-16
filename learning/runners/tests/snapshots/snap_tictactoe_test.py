# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots['test_tictactoe 1'] = 66

snapshots['test_tictactoe 2'] = {
    'id': 'test_id',
    'method': 'begin_training_run'
}

snapshots['test_tictactoe 3'] = {
    'method': 'debug',
    'msg': 'q_states_dims [3, 3, 3, 3, 3, 3, 3, 3, 3, 9]'
}

snapshots['test_tictactoe 4'] = {
    'initial_state': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    'iteration': 0,
    'method': 'begin_episode'
}

snapshots['test_tictactoe 5'] = {
    'action': GenericRepr('array([2, 1])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, 0, 0], [0, 0, -1], [0, 1, 0]],
    'step_iteration': 1
}

snapshots['test_tictactoe 6'] = {
    'action': GenericRepr('array([0, 2])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, 0, 1], [0, 0, -1], [0, 1, -1]],
    'step_iteration': 2
}

snapshots['test_tictactoe 7'] = {
    'action': (2, 1),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, 1], [0, 0, -1], [0, 1, -1]],
    'step_iteration': 3
}

snapshots['test_tictactoe 8'] = {
    'action': GenericRepr('array([2, 2])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, 1], [0, 0, -1], [0, 1, -1]],
    'step_iteration': 4
}

snapshots['test_tictactoe 9'] = {
    'action': GenericRepr('array([0, 2])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, 1], [0, 0, -1], [0, 1, -1]],
    'step_iteration': 5
}

snapshots['test_tictactoe 10'] = {
    'action': GenericRepr('array([1, 2])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, 1], [0, 0, -1], [0, 1, -1]],
    'step_iteration': 6
}

snapshots['test_tictactoe 11'] = {
    'action': GenericRepr('array([1, 0])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, -1, 1], [1, 0, -1], [0, 1, -1]],
    'step_iteration': 7
}

snapshots['test_tictactoe 12'] = {
    'action': (0, 2),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, -1, 1], [1, 0, -1], [0, 1, -1]],
    'step_iteration': 8
}

snapshots['test_tictactoe 13'] = {
    'action': GenericRepr('array([0, 0])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 9
}

snapshots['test_tictactoe 14'] = {
    'action': GenericRepr('array([2, 0])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 10
}

snapshots['test_tictactoe 15'] = {
    'action': GenericRepr('array([2, 1])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 11
}

snapshots['test_tictactoe 16'] = {
    'action': GenericRepr('array([1, 2])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 12
}

snapshots['test_tictactoe 17'] = {
    'action': GenericRepr('array([2, 1])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 13
}

snapshots['test_tictactoe 18'] = {
    'action': GenericRepr('array([2, 2])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 14
}

snapshots['test_tictactoe 19'] = {
    'action': GenericRepr('array([2, 1])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 15
}

snapshots['test_tictactoe 20'] = {
    'action': GenericRepr('array([0, 0])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 16
}

snapshots['test_tictactoe 21'] = {
    'action': GenericRepr('array([2, 2])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 17
}

snapshots['test_tictactoe 22'] = {
    'action': (0, 1),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 18
}

snapshots['test_tictactoe 23'] = {
    'action': GenericRepr('array([2, 2])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 19
}

snapshots['test_tictactoe 24'] = {
    'action': GenericRepr('array([0, 1])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 20
}

snapshots['test_tictactoe 25'] = {
    'action': GenericRepr('array([0, 1])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 21
}

snapshots['test_tictactoe 26'] = {
    'action': (1, 0),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 22
}

snapshots['test_tictactoe 27'] = {
    'action': GenericRepr('array([2, 1])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 23
}

snapshots['test_tictactoe 28'] = {
    'action': (0, 1),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[1, -1, 1], [1, 0, -1], [-1, 1, -1]],
    'step_iteration': 24
}

snapshots['test_tictactoe 29'] = {
    'action': GenericRepr('array([1, 1])'),
    'info': {},
    'is_done': True,
    'method': 'take_step',
    'reward': 0,
    'state': [[1, -1, 1], [1, 1, -1], [-1, 1, -1]],
    'step_iteration': 25
}

snapshots['test_tictactoe 30'] = {
    'iteration': 0,
    'method': 'end_episode',
    'total_reward': -5.999999999999998
}

snapshots['test_tictactoe 31'] = {
    'initial_state': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    'iteration': 1,
    'method': 'begin_episode'
}

snapshots['test_tictactoe 32'] = {
    'action': (1, 2),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[-1, 0, 0], [0, 0, 1], [0, 0, 0]],
    'step_iteration': 1
}

snapshots['test_tictactoe 33'] = {
    'action': GenericRepr('array([0, 1])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[-1, 1, 0], [0, -1, 1], [0, 0, 0]],
    'step_iteration': 2
}

snapshots['test_tictactoe 34'] = {
    'action': GenericRepr('array([2, 0])'),
    'info': {},
    'is_done': True,
    'method': 'take_step',
    'reward': -1,
    'state': [[-1, 1, 0], [0, -1, 1], [1, 0, -1]],
    'step_iteration': 3
}

snapshots['test_tictactoe 35'] = {
    'iteration': 1,
    'method': 'end_episode',
    'total_reward': -1
}

snapshots['test_tictactoe 36'] = {
    'initial_state': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    'iteration': 2,
    'method': 'begin_episode'
}

snapshots['test_tictactoe 37'] = {
    'action': GenericRepr('array([2, 1])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, 0, 0], [0, 0, -1], [0, 1, 0]],
    'step_iteration': 1
}

snapshots['test_tictactoe 38'] = {
    'action': GenericRepr('array([1, 1])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, -1, 0], [0, 1, -1], [0, 1, 0]],
    'step_iteration': 2
}

snapshots['test_tictactoe 39'] = {
    'action': GenericRepr('array([2, 1])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, -1, 0], [0, 1, -1], [0, 1, 0]],
    'step_iteration': 3
}

snapshots['test_tictactoe 40'] = {
    'action': (1, 0),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, -1, -1], [1, 1, -1], [0, 1, 0]],
    'step_iteration': 4
}

snapshots['test_tictactoe 41'] = {
    'action': (2, 0),
    'info': {},
    'is_done': True,
    'method': 'take_step',
    'reward': -1,
    'state': [[0, -1, -1], [1, 1, -1], [1, 1, -1]],
    'step_iteration': 5
}

snapshots['test_tictactoe 42'] = {
    'iteration': 2,
    'method': 'end_episode',
    'total_reward': -1.3
}

snapshots['test_tictactoe 43'] = {
    'initial_state': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    'iteration': 3,
    'method': 'begin_episode'
}

snapshots['test_tictactoe 44'] = {
    'action': (1, 2),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, 0, 0], [0, 0, 1], [0, -1, 0]],
    'step_iteration': 1
}

snapshots['test_tictactoe 45'] = {
    'action': (2, 2),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, 0, -1], [0, 0, 1], [0, -1, 1]],
    'step_iteration': 2
}

snapshots['test_tictactoe 46'] = {
    'action': (1, 0),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 3
}

snapshots['test_tictactoe 47'] = {
    'action': (0, 0),
    'info': {},
    'is_done': True,
    'method': 'take_step',
    'reward': -1,
    'state': [[1, -1, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 4
}

snapshots['test_tictactoe 48'] = {
    'iteration': 3,
    'method': 'end_episode',
    'total_reward': -1
}

snapshots['test_tictactoe 49'] = {
    'initial_state': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    'iteration': 4,
    'method': 'begin_episode'
}

snapshots['test_tictactoe 50'] = {
    'action': (1, 2),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, 0, 0], [0, 0, 1], [0, -1, 0]],
    'step_iteration': 1
}

snapshots['test_tictactoe 51'] = {
    'action': (2, 2),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, 0, -1], [0, 0, 1], [0, -1, 1]],
    'step_iteration': 2
}

snapshots['test_tictactoe 52'] = {
    'action': (1, 0),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': 0,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 3
}

snapshots['test_tictactoe 53'] = {
    'action': GenericRepr('array([2, 2])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 4
}

snapshots['test_tictactoe 54'] = {
    'action': GenericRepr('array([2, 2])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 5
}

snapshots['test_tictactoe 55'] = {
    'action': (0, 2),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 6
}

snapshots['test_tictactoe 56'] = {
    'action': (0, 2),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 7
}

snapshots['test_tictactoe 57'] = {
    'action': (1, 0),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 8
}

snapshots['test_tictactoe 58'] = {
    'action': (0, 2),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 9
}

snapshots['test_tictactoe 59'] = {
    'action': (2, 1),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 10
}

snapshots['test_tictactoe 60'] = {
    'action': (1, 0),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 11
}

snapshots['test_tictactoe 61'] = {
    'action': (0, 2),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 12
}

snapshots['test_tictactoe 62'] = {
    'action': (2, 1),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 13
}

snapshots['test_tictactoe 63'] = {
    'action': GenericRepr('array([1, 0])'),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 14
}

snapshots['test_tictactoe 64'] = {
    'action': (0, 2),
    'info': {},
    'is_done': False,
    'method': 'take_step',
    'reward': -0.3,
    'state': [[0, 0, -1], [1, -1, 1], [0, -1, 1]],
    'step_iteration': 15
}

snapshots['test_tictactoe 65'] = {
    'action': GenericRepr('array([2, 0])'),
    'info': {},
    'is_done': True,
    'method': 'take_step',
    'reward': -1,
    'state': [[0, -1, -1], [1, -1, 1], [1, -1, 1]],
    'step_iteration': 16
}

snapshots['test_tictactoe 66'] = {
    'iteration': 4,
    'method': 'end_episode',
    'total_reward': -4.6
}

snapshots['test_tictactoe 67'] = {'id': 'test_id', 'method': 'end_training_run'}
