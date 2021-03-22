from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
def root(request):
    return redirect('/blogs')

def index(request):
    return HttpResponse ("This is a placeholder to later display a list of all blogs.")

def new(request):
    return HttpResponse ("This is a placeholder to display a new form to create a new blog.")

def create(request):
    return redirect('/')

def show(request):
    return HttpResponse ("This is a placeholder to display a blog number: {number}")

def edit(request):
    return HttpResponse ("This is a placeholder to edit blog {number}")

def destroy(request):
    return redirect('/blogs')

def bonus(request):
    return JsonResponse({"response": "JSON response from", "status": True})