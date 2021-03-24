from django.shortcuts import render, redirect
from . models import Book, Author

# Create your views here.

def index(request):
    return redirect('/books')

def books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books.html', context)

def catalog_books(request):
    Book.objects.create(
        title = request.POST['book_title'],
        description = request.POST['book_description'],
    )
    return redirect('/books')

def display_books(request, book_id):
    correct_book = Book.objects.get(id = book_id)
    context = {
        'book_id' : correct_book
    }
    return render(request, "view_books.html", context)

def authors(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'authors.html', context)

def catalog_authors(request):
    Author.objects.create(
        first_name = request.POST['author_first_name'],
        last_name = request.POST['author_last_name'],
        notes = request.POST['author_notes'],
    )
    return redirect('/authors')
