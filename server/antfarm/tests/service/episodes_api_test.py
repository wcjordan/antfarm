import pytest
import unittest

from antfarm.tests.helpers.assert_helper import AnyArg
from antfarm.tests.helpers.generate_data import generate_random_string


def test_create_update(training_runs_fixture, episodes_fixture):
    """
    Basic test which creates and updates episodes
    and then fetches them to ensure they're persisted.
    """
    case = unittest.TestCase()  # define unittest so we can borrow its asserts

    run_id = training_runs_fixture.create({
        'name': generate_random_string(),
    })['id']
    ep1 = episodes_fixture.create({
        'iteration': 1,
        'total_reward': 0,
        'training_run': run_id,
    })['id']
    episodes_fixture.create({
        'iteration': 2,
        'total_reward': 0,
        'training_run': run_id,
    })

    fetched_data = episodes_fixture.fetch()
    expected_data = [{
        'id': AnyArg(),
        'iteration': 1,
        'total_reward': 0,
        'training_run': run_id
    }, {
        'id': AnyArg(),
        'iteration': 2,
        'total_reward': 0,
        'training_run': run_id
    }]
    case.assertCountEqual(fetched_data, expected_data)

    # Update ep1's reward
    patch = {
        'total_reward': 1.1,
    }
    episodes_fixture.update(ep1, patch)

    fetched_data = episodes_fixture.fetch()
    expected_data[0].update(patch)
    case.assertCountEqual(fetched_data, expected_data)
