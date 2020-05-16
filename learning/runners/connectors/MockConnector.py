class MockConnector:
    """
    Connector which records calls for testing
    """

    def __init__(self):
        self.log = []

    def debug(self, msg):
        """
        Record a debug message
        """
        self.log.append({'method': 'debug', 'msg': msg})

    def begin_training_run(self, id):
        """
        Record the start of a new episode and the initial state
        """
        self.log.append({'method': 'begin_training_run', 'id': id})

    def end_training_run(self, id):
        """
        Record the start of a new episode and the initial state
        """
        self.log.append({'method': 'end_training_run', 'id': id})

    def begin_episode(self, iteration, initial_state):
        """
        Record the start of a new episode and the initial state
        """
        self.log.append({
            'method': 'begin_episode',
            'iteration': iteration,
            'initial_state': initial_state
        })

    def end_episode(self, iteration, total_reward):
        """
        Record the end of the current episode
        and the total reward of the episode
        """
        self.log.append({
            'method': 'end_episode',
            'iteration': iteration,
            'total_reward': total_reward
        })

    def take_step(self, step_iteration, action, state, reward, is_done, info):
        """
        Take a step within the current episode
        Record the action taken, the outcome state, and the reward of the action
        Also includes a boolean if the action ends the episode
        and any debugging info
        """
        self.log.append({
            'method': 'take_step',
            'step_iteration': step_iteration,
            'action': action,
            'state': state,
            'reward': reward,
            'is_done': is_done,
            'info': info
        })

    def get_log(self):
        """
        Return the log
        """
        return self.log
