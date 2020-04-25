"""
Simple example which plays cart pole taking random actions
Doesn't use any learning agent, but does use OpenAI gym
"""
import argparse

import gym
from gym import logger


def run():
    """
    Play randomly!
    """
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('env_id',
                        nargs='?',
                        default='CartPole-v0',
                        help='Select the environment to run')
    args = parser.parse_args()

    # You can set the level to logger.DEBUG or logger.WARN if you
    # want to change the amount of output.
    logger.set_level(logger.INFO)

    env = gym.make(args.env_id)

    # Requires xvfb
    # You provide the directory to write to (can be an existing
    # directory, including one with existing data -- all monitor files
    # will be namespaced). You can also dump to a tempdir if you'd
    # like: tempfile.mkdtemp().
    # outdir = '/tmp/random-agent-results'
    # env = wrappers.Monitor(env, directory=outdir, force=True)
    env.seed(0)

    episode_count = 100
    done = False
    for _ in range(episode_count):
        env.reset()
        while True:
            action = env.action_space.sample()
            _, _, done, _ = env.step(action)
            if done:
                break
            # Note there's no env.render() here. But the environment still can
            # open window and render if asked by env.monitor: it calls
            # env.render('rgb_array') to record video. Video is not recorded
            # every episode, see capped_cubic_video_schedule for details.

    # Close the env and write monitor result info to disk
    env.close()


if __name__ == '__main__':
    run()
