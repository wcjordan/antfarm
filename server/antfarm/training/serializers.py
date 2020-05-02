"""
Django Rest Framework serializers for training models
"""
from rest_framework import serializers

from antfarm.training.models import (TrainingEpisodeModel, TrainingRunModel,
                                     TrainingStepModel)


class TrainingEpisodeSerializer(serializers.ModelSerializer):
    """
    Serializer for training episodes
    """

    class Meta:
        model = TrainingEpisodeModel
        fields = ['id', 'iteration', 'total_reward', 'training_run']


class TrainingRunSerializer(serializers.ModelSerializer):
    """
    Serializer for training runs
    """

    class Meta:
        model = TrainingRunModel
        fields = ['id', 'name', 'status']


class TrainingStepSerializer(serializers.ModelSerializer):
    """
    Serializer for training steps
    """

    class Meta:
        model = TrainingStepModel
        fields = [
            'id', 'iteration', 'action', 'state', 'reward', 'is_done', 'info',
            'episode'
        ]
