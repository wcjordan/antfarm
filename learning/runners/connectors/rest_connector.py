"""
Connector which submits data to a RESTful server
"""
import json
import requests

import numpy as np

DEFAULT_HEADERS = {'content-type': 'application/json'}


class RestConnector:
    """
    Connector which submits data to a RESTful server
    """

    def __init__(self, base_uri, run_uri, episode_uri, step_uri):
        self.base_uri = base_uri
        self.run_uri = run_uri
        self.episode_uri = episode_uri
        self.step_uri = step_uri

        self.current_run = None
        self.current_episode = None

    def debug(self, msg):  # pylint: disable=R0201
        """
        Record a debug message
        """
        # self._make_request('debug', 'POST', {
        #     'message': msg,
        #     'current_run': self.current_run,
        #     'current_episode': self.current_episode,
        # })
        print(msg)

    def begin_training_run(self, run_id):
        """
        Record the start of a new episode and the initial state
        """
        self._make_request(self.run_uri, 'PATCH', {
            'status': 'running',
        }, run_id)
        self.current_run = run_id

    def end_training_run(self, run_id):
        """
        Record the start of a new episode and the initial state
        """
        self._make_request(self.run_uri, 'PATCH', {
            'status': 'complete',
        }, run_id)
        self.current_run = None

    def begin_episode(self, iteration, initial_state):
        """
        Record the start of a new episode and the initial state
        """
        result = self._make_request(
            self.episode_uri, 'POST', {
                'iteration': iteration,
                'training_run': self.current_run,
                'total_reward': 0,
            })
        self.current_episode = result['id']
        self.take_step(0, None, initial_state, 0, False, None)

    def end_episode(self, total_reward):
        """
        Record the end of the current episode
        and the total reward of the episode
        """
        self._make_request(self.episode_uri, 'PATCH', {
            'total_reward': total_reward,
        }, self.current_episode)
        self.current_episode = None

    def take_step(self, step_iteration, action, state, reward, is_done, info):  # noqa  # pylint: disable=line-too-long,too-many-arguments
        """
        Take a step within the current episode
        Record the action taken, the outcome state, and the reward of the action
        Also includes a boolean if the action ends the episode
        and any debugging info
        """
        if isinstance(action, np.ndarray):
            action = action.tolist()

        self._make_request(
            self.step_uri, 'POST', {
                'iteration': step_iteration,
                'action': json.dumps(action),
                'state': json.dumps(state),
                'reward': reward,
                'is_done': is_done,
                'info': json.dumps(info),
                'episode': self.current_episode,
            })

    def _make_request(self, partial_uri, method, data, item_id=None):
        uri = '{}{}/'.format(self.base_uri, partial_uri)
        if item_id is not None:
            uri = '{}{}/'.format(uri, item_id)

        req = requests.request(method, uri, headers=DEFAULT_HEADERS, json=data)

        if req.status_code not in (200, 201):
            print(req.content)
        assert req.status_code in (200, 201), (
            'Expected status 2XX, received {}.'.format(req.status_code))
        return req.json()
