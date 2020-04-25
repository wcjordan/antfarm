"""
Simple example which plays tictactoe taking random actions
Doesn't use any learning agent, but does use OpenAI gym
"""
import time

import numpy as np
import gym


def run(episodes):
    """
    Play randomly!
    """
    env = gym.make('gym_tictactoe:tictactoe-v0')
    env.reset()

    # Initialize variables to track rewards
    reward_list = []
    ave_reward_list = []
    max_reward = float("-inf")

    for i in range(episodes):
        # Initialize parameters
        done = False
        tot_reward, reward = 0, 0
        env.reset()

        while not done:
            # Render environment for last 20 episodes and every 1000 episondes
            if i >= (episodes - 20) or i % 1000 == 0:
                time.sleep(.002)
                env.render()

            # Choose random action
            action = env.action_space.sample()

            # Get next state and reward
            _, reward, done, _ = env.step(action)

            # Update variables
            tot_reward += reward

        # Track rewards
        reward_list.append(tot_reward)
        if tot_reward > max_reward:
            max_reward = tot_reward
            print('New best score: {}'.format(max_reward))

        if (i + 1) % 100 == 0:
            ave_reward = np.mean(reward_list)
            ave_reward_list.append(ave_reward)
            reward_list = []
            print('Episode {} Average Reward: {}'.format(i + 1, ave_reward))

    env.close()


if __name__ == '__main__':
    run(5000)
