"""
Views for serving reinforcement learning details
"""

from rest_framework import permissions, viewsets

from antfarm.training.models import (TrainingEpisodeModel, TrainingRunModel,
                                     TrainingStepModel)
from antfarm.training.serializers import (TrainingEpisodeSerializer,
                                          TrainingRunSerializer,
                                          TrainingStepSerializer)


class TrainingEpisodeViewSet(viewsets.ModelViewSet):  # pylint: disable=R0901
    """
    API endpoint that allows viewing or editing an episode of a training run.
    """
    queryset = TrainingEpisodeModel.objects.all()
    serializer_class = TrainingEpisodeSerializer
    permission_classes = [permissions.AllowAny]  # permissions.IsAuthenticated


class TrainingRunViewSet(viewsets.ModelViewSet):  # pylint: disable=R0901
    """
    API endpoint that allows viewing or editing a training run.
    """
    queryset = TrainingRunModel.objects.all()
    serializer_class = TrainingRunSerializer
    permission_classes = [permissions.AllowAny]  # permissions.IsAuthenticated


class TrainingStepViewSet(viewsets.ModelViewSet):  # pylint: disable=R0901
    """
    API endpoint that allows viewing or editing a step of a training episode.
    """
    queryset = TrainingStepModel.objects.all()
    serializer_class = TrainingStepSerializer
    permission_classes = [permissions.AllowAny]  # permissions.IsAuthenticated
