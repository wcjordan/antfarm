from django.db import models


class EpisodeModel(models.Model):
    """An episode of training
    """
    name = models.TextField(unique=True)
    iteration = models.IntegerField()

    def __str__(self):
        return self.name
