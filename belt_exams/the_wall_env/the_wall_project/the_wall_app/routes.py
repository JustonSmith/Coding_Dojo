from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wall', views.wall),
    path('post', views.post_message),
    path('comment', views.post_comment),
    path('logout', views.logout),
    path('delete_message/<int:id>', views.delete_message),
    path('delete_comment/<int:id>', views.delete_comment),
]