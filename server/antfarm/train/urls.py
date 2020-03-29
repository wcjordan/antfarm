from django.conf.urls import url

from antfarm.train import views

urlpatterns = [
    url(r'^episodes$', views.episodes, name='episodes'),
]
