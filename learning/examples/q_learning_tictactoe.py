"""
Example which plays tictactoe using QLearning
Uses OpenAI gym
"""
import math
import time

import numpy as np
import gym

BOARD_SIZE = 3


def run_episodes(env, q_table, learning, discount, epsilon, min_eps, episodes):
    """
    Run training episodes
    """

    # Initialize variables to track rewards
    reward_list = []
    ave_reward_list = []
    max_reward = float("-inf")

    # Calculate episodic reduction in epsilon
    reduction = (epsilon - min_eps) / episodes

    # Run Q learning algorithm
    for episode_idx in range(episodes):
        # Initialize parameters
        done = False
        tot_reward, reward = 0, 0
        state = env.reset()

        # Discretize state (see q_learning_example for better example)
        state_adj = (state - env.observation_space.low)

        while not done:
            # Render environment for last 20 episodes and every 1000 episondes
            if ((episode_idx >= (episodes - 20) or episode_idx % 1000 == 0) and
                    reward != 0.3):
                time.sleep(.002)
                env.render()

            # Determine next action - epsilon greedy strategy
            if np.random.random() < 1 - epsilon:
                state_adj_tuple = tuple(np.ndarray.flatten(state_adj))
                flat_action = np.argmax(q_table[state_adj_tuple])
                action = (math.floor(flat_action / BOARD_SIZE),
                          flat_action % BOARD_SIZE)
            else:
                action = env.action_space.sample()
                flat_action = action[0] * BOARD_SIZE + action[1]

            # Get next state and reward
            state2, reward, done, _ = env.step(action)

            # Discretize state2
            state2_adj = (state2 - env.observation_space.low)
            state2_index = tuple(list(np.ndarray.flatten(state2_adj)))
            transition_list = list(np.ndarray.flatten(state_adj))
            transition_list.append(flat_action)
            transition_index = tuple(transition_list)

            # Allow for terminal states
            if done:
                q_table[transition_index] = reward

                if reward == 1:
                    print('You win!!!!!!!!!')
                elif reward == -1:
                    print('You LOSE!')

            # Adjust Q value for current state
            else:
                delta = learning * (reward +
                                    discount * np.max(q_table[state2_index]) -
                                    q_table[transition_index])
                q_table[transition_index] += delta

            # Update variables
            tot_reward += reward
            state_adj = state2_adj

        # Decay epsilon
        if epsilon > min_eps:
            epsilon -= reduction

        # Track rewards
        reward_list.append(tot_reward)
        if tot_reward > max_reward:
            max_reward = tot_reward
            print('New best score: {}'.format(max_reward))

        if (episode_idx + 1) % 100 == 0:
            ave_reward = np.mean(reward_list)
            ave_reward_list.append(ave_reward)
            reward_list = []
            print('Episode {} Average Reward: {}'.format(
                episode_idx + 1, ave_reward))


def q_learning_runner(learning, discount, epsilon, min_eps, episodes):
    """
    Train using QLearning algorithm
    """
    env = gym.make('gym_tictactoe:tictactoe-v0')
    env.reset()

    # Discretize the space (see q_learning_example for better example)
    # Number of states is observation state size: 3 states * number of cells
    # TODO derive this from env.observation_space
    num_states = np.array([3] * BOARD_SIZE * BOARD_SIZE)

    # Initialize Q table
    q_states_list = list(num_states)
    # Add a columns for listing actions
    # TODO derive this from env.action_space
    q_states_list.append(BOARD_SIZE * BOARD_SIZE)
    print(tuple(q_states_list))
    q_table = np.random.uniform(low=-1, high=1, size=tuple(q_states_list))

    run_episodes(env, q_table, learning, discount, epsilon, min_eps, episodes)
    env.close()


if __name__ == '__main__':
    q_learning_runner(0.2, 0.9, 0.8, 0, 1000)
