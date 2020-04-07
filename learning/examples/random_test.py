import time

import numpy as np
import gym


def RandomRunner(env, episodes):
    # Initialize variables to track rewards
    reward_list = []
    ave_reward_list = []
    max_reward = float("-inf")

    for i in range(episodes):
        # Initialize parameters
        done = False
        tot_reward, reward = 0, 0
        state = env.reset()
        
        while done != True:   
            # Render environment for last 20 episodes and every 1000 episondes
            if i >= (episodes - 20) or i % 1000 == 0:
                time.sleep(.002)
                env.render()
                
            # Choose random action
            action = env.action_space.sample()
                
            # Get next state and reward
            state2, reward, done, info = env.step(action) 
                                   
            # Update variables
            tot_reward += reward
                    
        # Track rewards
        reward_list.append(tot_reward)
        if tot_reward > max_reward:
            max_reward = tot_reward
            print('New best score: {}'.format(max_reward))
        
        if (i+1) % 100 == 0:
            ave_reward = np.mean(reward_list)
            ave_reward_list.append(ave_reward)
            reward_list = []
            print('Episode {} Average Reward: {}'.format(i+1, ave_reward))
            
    env.close()
    
    return ave_reward_list


if __name__ == '__main__':

    env = gym.make('gym_tictactoe:tictactoe-v0')
    env.reset()

    rewards = RandomRunner(env, 5000)
    env.close()
