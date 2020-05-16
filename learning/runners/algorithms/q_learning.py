import math
# import time

import numpy as np

BOARD_SIZE = 3


# Define Q-learning function
def QLearning(env,
              output_connector,
              learning,
              discount,
              epsilon,
              min_eps,
              episodes,
              seed=None):
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
    output_connector.debug('q_states_dims {}'.format(q_states_list))
    Q = np.random.uniform(low=-1, high=1, size=tuple(q_states_list))

    # Calculate episodic reduction in epsilon
    reduction = (epsilon - min_eps) / episodes

    # Run Q learning algorithm
    for episode_iteration in range(episodes):

        # Initialize parameters
        is_done = False
        tot_reward, reward = 0, 0
        state = env.reset()

        # Discretize state (see q_learning_example for better example)
        state_adj = (state - env.observation_space.low)

        output_connector.begin_episode(episode_iteration, state)
        step_iteration = 0
        while not is_done:
            step_iteration += 1

            # Render environment for last 20 episodes and every 1000 episondes
            # if (episode_iteration >= (episodes - 20) or
            #         episode_iteration % 1000 == 0) and reward != 0.3:
            #     time.sleep(.002)
            #     env.render()

            # Determine next action - epsilon greedy strategy
            if np.random.random() < 1 - epsilon:
                state_adj_tuple = tuple(np.ndarray.flatten(state_adj))
                flat_action = np.asscalar(np.argmax(Q[state_adj_tuple]))
                action = (math.floor(flat_action / BOARD_SIZE),
                          flat_action % BOARD_SIZE)
            else:
                action = env.action_space.sample()
                flat_action = action[0] * BOARD_SIZE + action[1]

            # Get next state and reward
            state2, reward, is_done, info = env.step(action)
            output_connector.take_step(step_iteration, action, state2, reward,
                                       is_done, info)

            # Discretize state2
            state2_adj = (state2 - env.observation_space.low)
            state2_index = tuple(list(np.ndarray.flatten(state2_adj)))
            transition_list = list(np.ndarray.flatten(state_adj))
            transition_list.append(flat_action)
            transition_index = tuple(transition_list)

            # Allow for terminal states
            if is_done:
                Q[transition_index] = reward

            # Adjust Q value for current state
            else:
                delta = learning * (reward + discount * np.max(Q[state2_index])
                                    - Q[transition_index])
                Q[transition_index] += delta

            # Update variables
            tot_reward += reward
            state_adj = state2_adj

        # Decay epsilon
        if epsilon > min_eps:
            epsilon -= reduction

        # Track rewards
        output_connector.end_episode(episode_iteration, tot_reward)

    env.close()
