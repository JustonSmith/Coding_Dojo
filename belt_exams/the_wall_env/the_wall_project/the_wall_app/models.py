from django.db import models

# Create your models here.

class User_Manager(models.Manager):
    def registration_validator(self, form_data):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$')
        if len(form_data['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(form_data['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if not email_regex.match(form_data['registration_email']):
            errors['registration_email'] = "Invalid email address."
        if len(form_data['registration_password']) < 8:
            errors['registration_password'] = "Password must be at least 8 characters"
        if form_data['registration_password'] != form_data['confirm_password']:
            errors['confirm_password'] = "passwords must match."
        return errors

    def login_validator(self, form_data):
        errors = {}
        email_regex = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$')
        if not email_regex.match(form_data['login_email']):
            errors['login_email'] = "Please enter a valid email address"
        if len(form_data['login_password']) == 0:
            errors['login_password'] = "Please enter password."
        return errors



class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email= models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = User_Manager()

class Message(models.Model):
        message_text = models.TextField()
        message_sender = models.ForeignKey(User, related_name = 'messages_sent', on_delete = models.CASCADE)
        created_at = models.DateTimeField(auto_now_add = True)
        updated_at = models. DateTimeField(auto_now = True)

class Comment(models.Model):
    comment_text = models.TextField()
    comment_poster = models.ForeignKey(User, related_name = 'comments_posted', on_delete = models.CASCADE)
    message_text = models.ForeignKey(Message, related_name = 'post_comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models. DateTimeField(auto_now = True)