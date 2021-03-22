from django.urls import path     
from . import views
urlpatterns = [
    path('', views.root),
    path('blogs', views.index)   # never put a preceeding slash
    path('blogs/new', views.new)
    path('blogs/create', views.create)
    path('blogs/<number>/edit', views.show)
    path('blogs/<number>/delete' views.destroy)
    path()
]

