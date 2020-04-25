"""
Django admin config for reinforcement learning training
"""
from django.contrib import admin

from antfarm.training import models

admin.site.register(models.TrainingRunModel)
admin.site.register(models.TrainingEpisodeModel)
admin.site.register(models.TrainingStepModel)
