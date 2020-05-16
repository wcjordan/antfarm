"""
QLearning algorithm for reinforcement learning
"""
import math
# import time

import numpy as np

BOARD_SIZE = 3
LEARNING_RATE = 0.2
DISCOUNT = 0.9
INIT_EPS = 0.8
MIN_EPS = 0


class QLearning:  # pylint: disable=too-few-public-methods
    """
    QLearning algorithm for reinforcement learning
    """

    def __init__(self, env, output_connector, seed=None):
        self.env = env
        self.output_connector = output_connector

        # Set the random seed for reproducibility if desired
        if seed is not None:
            np.random.seed(seed)

        # Discretize the space (see q_learning_example for better example)
        # Number of states is observation state size: 3 states * number of cells
        # TODO derive this from env.observation_space
        num_states = np.array([3] * BOARD_SIZE * BOARD_SIZE)

        # Initialize Q table
        q_states_list = list(num_states)
        # Add a columns for listing actions
        # TODO derive this from env.action_space
        q_states_list.append(BOARD_SIZE * BOARD_SIZE)
        self.output_connector.debug('q_states_dims {}'.format(q_states_list))
        self.q_table = np.random.uniform(low=-1,
                                         high=1,
                                         size=tuple(q_states_list))

    def train(self, episodes):
        """
        Run training episodes
        """
        # Calculate episodic reduction in epsilon
        reduction = (INIT_EPS - MIN_EPS) / episodes
        epsilon = INIT_EPS

        # Run Q learning algorithm
        for episode_iteration in range(episodes):

            # Initialize parameters
            is_done = False
            tot_reward, reward = 0, 0
            state = self.env.reset()

            # Discretize state (see q_learning_example for better example)
            state_adj = (state - self.env.observation_space.low)

            self.output_connector.begin_episode(episode_iteration, state)
            step_iteration = 0
            while not is_done:
                step_iteration += 1
                reward, state2_adj, is_done = self._learning_step(
                    state_adj, step_iteration, epsilon)

                # Update variables
                tot_reward += reward
                state_adj = state2_adj

            # Decay epsilon
            if epsilon > MIN_EPS:
                epsilon -= reduction

            # Track rewards
            self.output_connector.end_episode(tot_reward)

        self.env.close()

    def _learning_step(self, state_adj, step_iteration, epsilon):
        """
        Define a single learning step
        """
        # Render environment for last 20 episodes and every 1000 episondes
        # if (episode_iteration >= (episodes - 20) or
        #         episode_iteration % 1000 == 0) and reward != 0.3:
        #     time.sleep(.002)
        #     self.env.render()

        # Determine next action - epsilon greedy strategy
        if np.random.random() < 1 - epsilon:
            state_adj_tuple = tuple(np.ndarray.flatten(state_adj))
            flat_action = np.argmax(self.q_table[state_adj_tuple]).item()
            action = (math.floor(flat_action / BOARD_SIZE),
                      flat_action % BOARD_SIZE)
        else:
            action = self.env.action_space.sample()
            flat_action = action[0] * BOARD_SIZE + action[1]

        # Get next state and reward
        state2, reward, is_done, info = self.env.step(action)
        self.output_connector.take_step(step_iteration, action, state2, reward,
                                        is_done, info)

        # Discretize state2
        state2_adj = (state2 - self.env.observation_space.low)
        state2_index = tuple(list(np.ndarray.flatten(state2_adj)))
        transition_index = list(np.ndarray.flatten(state_adj))
        transition_index.append(flat_action)
        transition_index = tuple(transition_index)

        # Allow for terminal states
        if is_done:
            self.q_table[transition_index] = reward

        # Adjust Q value for current state
        else:
            delta = LEARNING_RATE * (
                reward + DISCOUNT * np.max(self.q_table[state2_index]) -
                self.q_table[transition_index])
            self.q_table[transition_index] += delta

        return reward, state2_adj, is_done
