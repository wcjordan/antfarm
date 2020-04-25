"""
Django ORM models for reinforcement learning training
"""
from django.db import models


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
