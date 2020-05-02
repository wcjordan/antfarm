"""
Url routing for reinforcement learning models
"""
from django.urls import include, path
from rest_framework import routers

from antfarm.training import views

router = routers.DefaultRouter()
router.register('episodes', views.TrainingEpisodeViewSet)
router.register('steps', views.TrainingStepViewSet)
router.register('training_runs', views.TrainingRunViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
