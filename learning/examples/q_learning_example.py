"""
Example which plays mountain car using QLearning
Uses OpenAI gym
"""
import numpy as np
import gym


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

        # Discretize state
        state_adj = (state - env.observation_space.low) * np.array([10, 100])
        state_adj = np.round(state_adj, 0).astype(int)

        while not done:
            # Render environment for last 20 episodes and every 1000 episondes
            # Requires xvfb
            # if episode_idx >= (episodes - 20) or episode_idx % 1000 == 0:
            #     time.sleep(.002)
            #     env.render()

            # Determine next action - epsilon greedy strategy
            if np.random.random() < 1 - epsilon:
                action = np.argmax(q_table[state_adj[0], state_adj[1]])
            else:
                action = np.random.randint(0, env.action_space.n)

            # Get next state and reward
            state2, reward, done, _ = env.step(action)

            # Discretize state2
            state2_adj = (state2 - env.observation_space.low) * np.array(
                [10, 100])
            state2_adj = np.round(state2_adj, 0).astype(int)

            # Allow for terminal states
            if done and state2[0] >= 0.5:
                q_table[state_adj[0], state_adj[1], action] = reward

            # Adjust Q value for current state
            else:
                delta = learning * (
                    reward +
                    discount * np.max(q_table[state2_adj[0], state2_adj[1]]) -
                    q_table[state_adj[0], state_adj[1], action])
                q_table[state_adj[0], state_adj[1], action] += delta

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

    env.close()

    return ave_reward_list


def q_learning_runner(learning, discount, epsilon, min_eps, episodes):
    """
    Train using QLearning algorithm
    """
    env = gym.make('MountainCar-v0')
    env.reset()

    # Determine size of discretized state space
    num_states = (env.observation_space.high -
                  env.observation_space.low) * np.array([10, 100])
    num_states = np.round(num_states, 0).astype(int) + 1

    # Initialize Q table
    q_table = np.random.uniform(low=-1,
                                high=1,
                                size=(num_states[0], num_states[1],
                                      env.action_space.n))

    run_episodes(env, q_table, learning, discount, epsilon, min_eps, episodes)
    env.close()


if __name__ == '__main__':
    q_learning_runner(0.2, 0.9, 0.8, 0, 1000)
