"""
Tests for training module
"""
import collections

from django.test import TestCase
import responses

from antfarm.training.models import _execute_after_save

TrainingRunStub = collections.namedtuple('TrainingRunStub', 'name id')


class ModelsTests(TestCase):
    """
    Tests for models
    """

    @responses.activate
    def test_execute_after_save(self):
        """
        Test for submission to training service after a training run is created
        """
        responses.add(
            responses.POST,
            'http://learning:8000/start_training_run',
            status=204,
        )

        run = TrainingRunStub(name='Stubbed run', id=101)
        _execute_after_save(None, run, True)

        self.assertEqual(len(responses.calls), 1)
        self.assertEqual(responses.calls[0].request.url,
                         'http://learning:8000/start_training_run')
        self.assertEqual(responses.calls[0].request.body, b'{"id": 101}')
