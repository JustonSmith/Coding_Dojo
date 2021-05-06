from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('openmics', views.openmics),
    path('logout', views.logout),
    path('openmics/create', views.openmics_create),
    path('openmics/<int:openmic_id>/edit', views.openmics_edit),
    path('openmics/<int:openmics_id>', views.openmics_display),
]