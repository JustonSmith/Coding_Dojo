from django.shortcuts import render, redirect
from . models import Dojo, Ninja

# Create your views here.

def index(request):
    all_dojos = Dojo.objects.all()
    context = {
        'all_dojos' = all_dojos
    }
    return render(request, 'index.html', context) 

def dojo_create(request):
    Dojo.objects.create(
        name = request.POST['name']
        city = request.POST['city']
        state = request.POST['state']
    )
    return redirect('/')

def ninja_create(request):
    dojo = Dojo.object.get(id = request.post['dojo_id'])
    Ninja.objects.create(
        first_name = request.POST['first_name']
        last_name= request.POST['last_name']
        dojo = dojo
    )
    return redirect('/')