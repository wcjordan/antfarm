"""
Django ORM models for reinforcement learning training
"""
import requests

from django.db import models
from django.dispatch import receiver


class TrainingRunModel(models.Model):
    """A training run
    """
    name = models.TextField(unique=True)
    status = models.TextField(default="new")

    def __str__(self):
        return '{} ({})'.format(self.name, self.status)


class TrainingEpisodeModel(models.Model):
    """An episode of a training run
    """
    iteration = models.IntegerField()
    total_reward = models.FloatField()

    training_run = models.ForeignKey(TrainingRunModel,
                                     on_delete=models.CASCADE,
                                     related_name='episode_set')

    def __str__(self):
        return '{}: Episode {}'.format(self.training_run, self.iteration)

    class Meta:
        unique_together = ('training_run', 'iteration')


class TrainingStepModel(models.Model):
    """An single step of a training episode
    """
    iteration = models.IntegerField()
    action = models.TextField(null=True)
    state = models.TextField()
    reward = models.FloatField()
    is_done = models.BooleanField()
    info = models.TextField(null=True)

    episode = models.ForeignKey(TrainingEpisodeModel,
                                on_delete=models.CASCADE,
                                related_name='step_set')

    def __str__(self):
        return '{} - Step {}'.format(self.episode, self.iteration)

    class Meta:
        unique_together = ('episode', 'iteration')


def _make_learning_service_request(training_run_id):
    data = {
        'id': training_run_id,
    }
    headers = {
        'content-type': 'application/json',
    }
    req = requests.post('http://learning:8000/start_training_run',
                        headers=headers,
                        json=data)

    assert req.status_code == 204, 'Expected status 204, received {}.'.format(
        req.status_code)


@receiver(models.signals.post_save, sender=TrainingRunModel)
def _execute_after_save(_, instance, created):
    if created:
        print('Created new training run: {} ({})'.format(
            instance.name, instance.id))
        _make_learning_service_request(instance.id)
