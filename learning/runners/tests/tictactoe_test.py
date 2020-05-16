"""
Snapshot testing to ensure tictactoe learning doesn't regress
"""
from connectors.mock_connector import MockConnector

from tictactoe import run_tictactoe

RANDOM_SEED = 211


def test_tictactoe(snapshot):
    """
    Test a game of tictactoe doesn't regress
    """
    # Create a connector to record training data
    output_connector = MockConnector()

    # Run training algorithm
    run_tictactoe(output_connector, 'test_id', episodes=5, seed=RANDOM_SEED)

    # Assert snapshots match
    log = output_connector.get_log()
    snapshot.assert_match(len(log))
    for log_entry in log:
        snapshot.assert_match(log_entry)
