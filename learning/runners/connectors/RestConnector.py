import requests

import numpy as np

DEFAULT_HEADERS = {'content-type': 'application/json'}

class RestConnector:
    '''Connector which submits data to a RESTful server
    '''

    def __init__(self, base_uri, run_uri, episode_uri, step_uri):
        self.base_uri = base_uri
        self.run_uri = run_uri
        self.episode_uri = episode_uri
        self.step_uri = step_uri

        self.current_run = None
        self.current_episode = None

    def debug(self, msg):
        ''' Record a debug message
        '''
        # self._make_request('debug', 'POST', {
        #     'message': msg,
        #     'current_run': self.current_run,
        #     'current_episode': self.current_episode,
        # })
        print(msg)
        
    def begin_training_run(self, name):
        ''' Record the start of a new episode and the initial state
        '''
        result = self._make_request(self.run_uri, 'POST', {
            'name': name,
        })
        self.current_run = result['id']

    def begin_episode(self, iteration, initial_state):
        ''' Record the start of a new episode and the initial state
        '''
        result = self._make_request(self.episode_uri, 'POST', {
            'iteration': iteration,
            'training_run_id': self.current_run,
        })
        self.current_episode = result['id']
        self.take_step(0, None, initial_state, 0, False, None)

    def end_episode(self, iteration, total_reward):
        ''' Record the end of the current episode
        and the total reward of the episode
        '''
        self._make_request(self.episode_uri, 'PUT', {
            'total_reward': total_reward,
        }, self.current_episode)
        self.current_episode = None

    def take_step(self, step_iteration, action, state, reward, is_done, info):
        ''' Take a step within the current episode
        Record the action taken, the outcome state, and the reward of the action
        Also includes a boolean if the action ends the episode
        and any debugging info
        '''
        if isinstance(action, np.ndarray):
            action = action.tolist()

        self._make_request(self.step_uri, 'POST', {
            'iteration': step_iteration,
            'action': action,
            'state': state,
            'reward': reward,
            'is_done': is_done,
            'info': info,
            'episode_id': self.current_episode,
        })

    def _make_request(self, partial_uri, method, data, id=None):
        headers = {
            'X-HTTP-Method-Override': method,
        }
        headers.update(DEFAULT_HEADERS)

        uri = '{}{}'.format(self.base_uri, partial_uri)
        if id is not None:
            uri = '{}/{}'.format(uri, id)

        req = requests.post(
            uri,
            headers=headers,
            json=data)

        assert req.status_code == 200, 'Expected status 200, received {}.'.format(req.status_code)
        return req.json()

