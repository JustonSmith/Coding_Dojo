from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, OpenMic, Comment
import re
import bcrypt
email_regex = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$')

# Create your views here.

def index(request):
    return render(request, "index.html")

def register(request):
    errors = User.objects.registration_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            if key == 'first_name':
                messages.error(request, value,  extra_tags = 'first_name')
            if key == 'last_name':
                messages.error(request, value,  extra_tags = 'last_name')
            if key == 'registration_email':
                messages.error(request, value,  extra_tags = 'registration_email')
            if key == 'registration_password':
                messages.error(request, value,  extra_tags = 'registration_password')
            if key == 'confirm_password':
                messages.error(request, value,  extra_tags = 'confirm_password')
        return redirect('/')
    else:
        hashed_password = bcrypt.hashpw(request.POST['registration_password'].encode(), bcrypt.gensalt())
        user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['registration_email'],
            password = hashed_password
        )
        request.session['user_id'] = user.id
        return redirect('/openmics')

def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            if key == 'login_email':
                messages.error(request, value, extra_tags = 'login_email')
            if key == 'login_password':
                messages.error(request, value, extra_tags = 'login_password')
        return redirect('/')
    else:
        user_list = User.objects.filter(email = request.POST['login_email'])
        if len(user_list) == 0:
            messages.error(request, 'Sorry, a user with that address was not found. Please use valid email, or register an account.', extra_tags = 'login_email')
            return redirect('/')
        else:
            user = user_list[0]
            if bcrypt.checkpw(request.POST['login_password']. encode(),user.password.encode()):
                request.session['user_id'] = user.id
                return redirect('/openmics')
            else:
                messages.error(request, 'Sorry, the password you entered was incorrect. Please try again.', extra_tags = 'login_password')
                return redirect('/')

def openmics(request):
    if 'is_first_timer' not in request.session:
        request.session['is_first_timer'] = False
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context = {
            'user': User.objects.get(id = request.session['user_id']),
            'openmics': OpenMic.objects.all()
        }
        return render(request, 'openmics.html', context)

def openmics_create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    if request.method == 'POST':
        errors = OpenMic.objects.openmic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            if key == 'venue':
                messages.error(request, value,  extra_tags = 'venue')
            if key == 'genre':
                messages.error(request, value,  extra_tags = 'genre')
            if key == 'date':
                messages.error(request, value,  extra_tags = 'date')
            if key == 'description':
                messages.error(request, value,  extra_tags = 'description')
        return redirect('/openmics/create')
    else:
        user = User.objects.get(id = request.session['user_id'])
        openmic = OpenMic.objects.create(
            venue = request.POST['venue'],
            genre = request.POST['genre'],
            date = request.POST['date'],
            description = request.POST['description'],
            creator = user
        )
        openmic.performers.add(user)
        return redirect('/openmics')

def openmics_edit(request, openmic_id):
    if request.method == 'GET':
        context = {
            'openmic': OpenMic.objects.get(id = openmic_id)
        }
    return render(request, 'edit.html')
    if request.method == 'POST':
        errors = OpenMic.objects.openmic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            if key == 'venue':
                messages.error(request, value,  extra_tags = 'venue')
            if key == 'genre':
                messages.error(request, value,  extra_tags = 'genre')
            if key == 'date':
                messages.error(request, value,  extra_tags = 'date')
            if key == 'description':
                messages.error(request, value,  extra_tags = 'description')
        return redirect(f'/openmics/{openmic.id}/edit')
    else:
        openmic = OpenMic.objects.get(id = openmic_id)
        openmic.venue = request.POST['venue']
        openmic.genre = request.POST['genre']
        openmic.date = request.POST ['date']
        openmic.description = request.POST['description']
        openmic.save()
        return redirect(f'/openmics/{openmic.id}')

def openmics_display(request):
    context = {
        'openmic': OpenMic.objects.get(id = openmic_id)
    }
    return render(request, 'display.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')



