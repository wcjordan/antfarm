import pytest
import unittest

from antfarm.tests.helpers.assert_helper import AnyArg
from antfarm.tests.helpers.generate_data import generate_random_string


def test_create_update(training_runs_fixture):
    """
    Basic test which creates and updates training runs
    and then fetches them to ensure they're persisted.
    """
    case = unittest.TestCase()  # define unittest so we can borrow its asserts
    run1_name = generate_random_string()
    run2_name = generate_random_string()

    run1_id = training_runs_fixture.create({
        'name': run1_name,
    })['id']
    training_runs_fixture.create({
        'name': run2_name,
        'status': 'complete',
    })

    fetched_data = training_runs_fixture.fetch()
    expected_data = [{
        'id': AnyArg(),
        'name': run1_name,
        'status': 'new',
    }, {
        'id': AnyArg(),
        'name': run2_name,
        'status': 'complete',
    }]
    case.assertCountEqual(fetched_data, expected_data)

    # Update run1 to be complete
    patch = {
        'status': 'complete',
    }
    training_runs_fixture.update(run1_id, patch)

    fetched_data = training_runs_fixture.fetch()
    expected_data[0].update(patch)
    case.assertCountEqual(fetched_data, expected_data)
