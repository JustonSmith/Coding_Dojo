from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
import re
email_regex = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$')

# Create your views here.

def index(request):
    return render(request, "index.html" )

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
        new_user = User.objects.create(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            password = hashed_password
        )
        request.session['user_id'] = new_user.id
        return redirect('/the_wall')

def login(request):
    errors = User.objects. login_validator(request.POST)
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
            messages.error(request, 'Sorry, a user with that address whas not found. Please use valid email, or register an account.')
            return redirect('/')
        else:
            user = user_list[0]
            if bcrypt.checkpw(
                request.POST['login_password']. encode(),
                user.password.encode()
            ):
            request.session['user_id'] = user.id
            return redirect('/the_wall')
        else:
            messages.error(request, 'Sorry, the password you entered was incorrect. Please try again.')

def wall(request):
    context = {
        'posts' : Message.objects.all(), 
    }
    return render(request, 'the_wall.html', context)

def post_message(request):
    Message.objects.create(message = request.POST['message_text'], message_sender = User.objects.get(id = request.session['user_id']))
    return redirect('/the_wall')
    print(request.POST['message_text'])

def post_comment(request):
    Comment.objects.create(comment = request.POST['comment_text'], comment_poster = User.objects.get(id = request.session['user_id']), post = Message.objects.get(id = request.POST['comment_poster']))
    return redirect('/wall')
    print(request.POST['comment'])

def logout(request):
    request.session.flush()
    return redirect('/')

def delete_message(request, id):
    Message.objects.get(id = request.post['message_sender']).delete()
    return redirect('/wall')

def delete_comment( request, id):
    Comment.objects.get(id = request.POST['comment_poster']).delete()
    return redirect('/wall')



