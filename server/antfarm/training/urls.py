from django.conf.urls import url

from antfarm.training import views

urlpatterns = [
    url(r'^episodes$', views.episodes, name='episodes'),
]
