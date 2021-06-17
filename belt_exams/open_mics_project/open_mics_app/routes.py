from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('openmics', views.openmics),
    path('logout', views.logout),
    path('openmics/create', views.openmics_create),
    path('openmics/<int:openmics_id>/edit', views.openmics_edit),
    path('openmics/<int:openmics_id>', views.openmics_display),
    path('comment', views.comment)
    path('signup', views.signup)
    path('cancel', views.cancel)
    # path('post_view', views.post_view)
    # path('like_view', views.like_view)
]