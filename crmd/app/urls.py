from django.urls import path
from django.conf.urls import url
from app import views

urlpatterns = [
  url(r'^details', views.debate_details, name='details'),
  url(r'^scores', views.scores, name='scores')
]