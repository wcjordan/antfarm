import pytest
import unittest

from antfarm.tests.helpers.assert_helper import AnyArg
from antfarm.tests.helpers.generate_data import generate_random_string


def test_create_update(training_runs_fixture, episodes_fixture, steps_fixture):
    """
    Basic test which creates and updates episodes
    and then fetches them to ensure they're persisted.
    """
    case = unittest.TestCase()  # define unittest so we can borrow its asserts

    run_id = training_runs_fixture.create({
        'name': generate_random_string(),
    })['id']
    episode_id = episodes_fixture.create({
        'iteration': 1,
        'total_reward': 1,
        'training_run': run_id,
    })['id']

    step1 = steps_fixture.create({
        'iteration': 1,
        'action': None,
        'state': '[0, 0]',
        'reward': 0.1,
        'is_done': False,
        'info': None,
        'episode': episode_id,
    })['id']
    steps_fixture.create({
        'iteration': 2,
        'action': 'N',
        'state': '[0, 1]',
        'reward': 0.4,
        'is_done': True,
        'info': "{'warnings': 'true'}",
        'episode': episode_id,
    })

    fetched_data = steps_fixture.fetch()
    expected_data = [{
        'id': AnyArg(),
        'iteration': 1,
        'action': None,
        'state': '[0, 0]',
        'reward': 0.1,
        'is_done': False,
        'info': None,
        'episode': episode_id,
    }, {
        'id': AnyArg(),
        'iteration': 2,
        'action': 'N',
        'state': '[0, 1]',
        'reward': 0.4,
        'is_done': True,
        'info': "{'warnings': 'true'}",
        'episode': episode_id,
    }]
    case.assertCountEqual(fetched_data, expected_data)

    # Update step1
    patch = {
        'reward': 0.2,
        'state': '[1, 1]',
    }
    steps_fixture.update(step1, patch)

    fetched_data = steps_fixture.fetch()
    expected_data[0].update(patch)
    case.assertCountEqual(fetched_data, expected_data)
