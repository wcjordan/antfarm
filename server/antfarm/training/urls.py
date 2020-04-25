"""
Url routing for reinforcement learning models
"""
from django.conf.urls import url

from antfarm.training import views

urlpatterns = [
    url(r'^episodes$', views.episodes, name='episodes'),
    url(r'^episodes/(?P<id>\d+)$', views.episode, name='episode'),
    url(r'^steps$', views.steps, name='steps'),
    url(r'^training_runs$', views.training_runs, name='training_runs'),
]
