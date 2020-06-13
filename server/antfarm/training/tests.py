"""
Tests for training module
"""
import random
import string

from django.test import TestCase
import responses


class AnyArg():  # pylint: disable=R0903
    """
    Arg matcher which matches everything
    """

    def __eq__(self, other):
        return True


def _generate_random_string():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))


class ServiceTests(TestCase):
    """
    Tests for training run view
    """

    @responses.activate
    def test_training_runs_api(self):
        """
        Basic test which creates and updates training runs
        and then fetches them to ensure they're persisted.
        """
        run1_name = _generate_random_string()
        run2_name = _generate_random_string()

        # Mock response libary to capture calls to learning service
        responses.add(
            responses.POST,
            'http://learning:8000/start_training_run',
            status=204,
        )

        # Create an training run
        run1_id = self._create_training_run({
            'name': run1_name,
        })['id']

        # Verify call to learning service to start training took place
        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url,
                         'http://learning:8000/start_training_run')
        self.assertEqual(responses.calls[0].request.body,
                         '{{"id": {}}}'.format(run1_id).encode())

        # Create another training run
        run2_id = self._create_training_run({
            'name': run2_name,
            'status': 'complete',
        })['id']

        # Verify call to learning service to start training took place
        self.assertEqual(len(responses.calls), 2)
        self.assertEqual(responses.calls[1].request.url,
                         'http://learning:8000/start_training_run')
        self.assertEqual(responses.calls[1].request.body,
                         '{{"id": {}}}'.format(run2_id).encode())

        # Fetch training runs and verify they match expectations
        fetched_data = self._fetch_training_runs()
        expected_data = [{
            'id': AnyArg(),
            'name': run1_name,
            'status': 'new',
        }, {
            'id': AnyArg(),
            'name': run2_name,
            'status': 'complete',
        }]
        self.assertCountEqual(fetched_data, expected_data)

        # Update first training run to be complete
        patch = {
            'status': 'complete',
        }
        self._update_training_run(run1_id, patch)

        # Fetch training runs and verify they match expectations
        fetched_data = self._fetch_training_runs()
        expected_data[0].update(patch)
        self.assertCountEqual(fetched_data, expected_data)

        # Delete first training run
        self._delete_training_run(run1_id)

        # Fetch training runs and verify they match expectations
        fetched_data = self._fetch_training_runs()
        expected_data = [expected_data[1]]
        self.assertCountEqual(fetched_data, expected_data)

    @responses.activate
    def test_episodes_api(self):
        """
        Basic test which creates and updates episodes
        and then fetches them to ensure they're persisted.
        """
        # Create a training run to contain episodes
        # Includes mocking response libary to capture calls to learning service
        responses.add(
            responses.POST,
            'http://learning:8000/start_training_run',
            status=204,
        )
        run_id = self._create_training_run({
            'name': _generate_random_string(),
        })['id']

        # Create 2 episodes
        ep1 = self._create_episode({
            'iteration': 1,
            'total_reward': 0,
            'training_run': run_id,
        })['id']
        self._create_episode({
            'iteration': 2,
            'total_reward': 0,
            'training_run': run_id,
        })

        # Fetch episodes and verify they match expectations
        fetched_data = self._fetch_episodes()
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
        self.assertCountEqual(fetched_data, expected_data)

        # Update the first episode's reward
        patch = {
            'total_reward': 1.1,
        }
        self._update_episode(ep1, patch)

        # Fetch episodes and verify they match expectations
        fetched_data = self._fetch_episodes()
        expected_data[0].update(patch)
        self.assertCountEqual(fetched_data, expected_data)

        # Delete first episode
        self._delete_episode(ep1)

        # Fetch episodes and verify they match expectations
        fetched_data = self._fetch_episodes()
        expected_data = [expected_data[1]]
        self.assertCountEqual(fetched_data, expected_data)

    @responses.activate
    def test_steps_api(self):
        """
        Basic test which creates and updates steps
        and then fetches them to ensure they're persisted.
        """
        # Create a training run & episode to contain steps
        # Includes mocking response libary to capture calls to learning service
        responses.add(
            responses.POST,
            'http://learning:8000/start_training_run',
            status=204,
        )
        run_id = self._create_training_run({
            'name': _generate_random_string(),
        })['id']
        episode_id = self._create_episode({
            'iteration': 1,
            'total_reward': 1,
            'training_run': run_id,
        })['id']

        # Create 2 steps
        step1 = self._create_step({
            'iteration': 1,
            'action': None,
            'state': '[0, 0]',
            'reward': 0.1,
            'is_done': False,
            'info': None,
            'episode': episode_id,
        })['id']
        self._create_step({
            'iteration': 2,
            'action': 'N',
            'state': '[0, 1]',
            'reward': 0.4,
            'is_done': True,
            'info': "{'warnings': 'true'}",
            'episode': episode_id,
        })

        # Fetch episodes and verify they match expectations
        fetched_data = self._fetch_steps()
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
        self.assertCountEqual(fetched_data, expected_data)

        # Update the first step
        patch = {
            'reward': 0.2,
            'state': '[1, 1]',
        }
        self._update_step(step1, patch)

        # Fetch steps and verify they match expectations
        fetched_data = self._fetch_steps()
        expected_data[0].update(patch)
        self.assertCountEqual(fetched_data, expected_data)

        # Delete first step
        self._delete_step(step1)

        # Fetch steps and verify they match expectations
        fetched_data = self._fetch_steps()
        expected_data = [expected_data[1]]
        self.assertCountEqual(fetched_data, expected_data)

    def _create_training_run(self, data):
        return self._create_entity(data, 'training_runs')

    def _fetch_training_runs(self):
        return self._fetch_entity('training_runs')

    def _update_training_run(self, entry_id, patch):
        return self._update_entity(entry_id, patch, 'training_runs')

    def _delete_training_run(self, entry_id):
        return self._delete_entity(entry_id, 'training_runs')

    def _create_episode(self, data):
        return self._create_entity(data, 'episodes')

    def _fetch_episodes(self):
        return self._fetch_entity('episodes')

    def _update_episode(self, entry_id, patch):
        return self._update_entity(entry_id, patch, 'episodes')

    def _delete_episode(self, entry_id):
        return self._delete_entity(entry_id, 'episodes')

    def _create_step(self, data):
        return self._create_entity(data, 'steps')

    def _fetch_steps(self):
        return self._fetch_entity('steps')

    def _update_step(self, entry_id, patch):
        return self._update_entity(entry_id, patch, 'steps')

    def _delete_step(self, entry_id):
        return self._delete_entity(entry_id, 'steps')

    def _create_entity(self, data, route):
        response = self.client.post('/api/training/{}/'.format(route),
                                    data,
                                    content_type='application/json')
        self._assert_status_code(201, response)
        return response.json()

    def _fetch_entity(self, route):
        response = self.client.get('/api/training/{}/'.format(route))
        self._assert_status_code(200, response)
        return response.json()

    def _update_entity(self, entry_id, patch, route):
        response = self.client.patch('/api/training/{}/{}/'.format(
            route, entry_id),
                                     patch,
                                     content_type='application/json')
        self._assert_status_code(200, response)
        return response.json()

    def _delete_entity(self, entry_id, route):
        response = self.client.delete('/api/training/{}/{}/'.format(
            route, entry_id))
        self._assert_status_code(204, response)

    def _assert_status_code(self, expected_code, response):
        self.assertEqual(
            response.status_code, expected_code,
            'Expected status {}, received {}'.format(expected_code,
                                                     response.status_code))
