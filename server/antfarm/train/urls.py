from django.conf.urls import url

from antfarm.train.views import episode_views

urlpatterns = [
    url(r'^episodes$', episode_views.episodes, name='episodes'),
]
