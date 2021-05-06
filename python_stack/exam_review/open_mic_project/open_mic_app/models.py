from django.db import models
import re
email_regex = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$')

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

class OpenMic_Manager(models.Manager):
    def openmic_validator(self, form_data):
        errors = {}
        if len(form_data['venue']) < 2:
            errors['venue'] = "Venue must be at least 2 characters."
        if len(form_data['genre']) < 2:
            errors['genre'] = "Genre must be at least 2 characters."
        if len(form_data['date']) == 0:
            errors['date'] = "Please enter date."
        if len(form_data['description']) < 10:
            errors['description'] = "Description should be at least 10 characters."
        return errors 

class Comment_Manager(models.Manager):
    def comment_validator(self, form_data):
        errors = {}
        if len(form_data['content']) < 10:
            errors['content'] = "comment should be at least 10 characters."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email= models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = User_Manager()

class OpenMic(models.Model):
    venue = models.CharField(max_length = 45)
    genre = models.CharField(max_length = 45)
    date = models.DateTimeField()
    description = models.TextField()
    post_creator = models.ForeignKey(User, related_name = 'openmics', on_delete = models.CASCADE)
    performers = models.ManyToManyField(User, related_name = 'performances')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = OpenMic_Manager()

class Comment(models.Model):
    content = models.TextField()
    posted_by = models.ForeignKey(User, related_name = 'comments', on_delete = models.CASCADE)
    openmic = models.ForeignKey(OpenMic, related_name = 'comments', on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = Comment_Manager()


