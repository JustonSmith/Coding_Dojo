from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/', views.books),
    path('catalog_books', views.catalog_books),
    path('book/<int:book_id>', views.display_books),
    path('authors/', views.authors),
    path('catalog_authors', views.catalog_authors),
]