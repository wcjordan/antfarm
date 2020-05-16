import gym

from algorithms.q_learning import QLearning
from connectors.MockConnector import MockConnector

RANDOM_SEED = 211


def test_tictactoe(snapshot):
    """
    Test a game of tictactoe doesn't regress
    """
    env = gym.make('gym_tictactoe:tictactoe-v0')
    env.reset()
    env.seed(RANDOM_SEED)

    # Create a connector to record training data
    output_connector = MockConnector()
    output_connector.begin_training_run('test_id')

    # Run Q-learning algorithm
    QLearning(env, output_connector, 0.2, 0.9, 0.8, 0, 5, seed=RANDOM_SEED)
    env.close()
    output_connector.end_training_run('test_id')

    log = output_connector.get_log()
    snapshot.assert_match(len(log))
    for log_entry in log:
        snapshot.assert_match(log_entry)
