from django.urls import path
from . import views

urlpatterns = [
    path('process', views.process),
    path('results', views.results),
    path('', views.index),
]
