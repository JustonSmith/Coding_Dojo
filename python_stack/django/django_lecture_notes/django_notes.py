

##_______DJANGO_______##

# creating django project #

# Remember that a single application in Django (in our case, every assignment) is called a project, which contains one or more apps.

# With our Django virtual environment activated, create a new Django project. First navigate to where you want the project to be saved (for these first few assignments, that will be the python_stack/django/django_intro folder). Then run this command, specifying a project name of our choosing:

# cd python_stack/django/django_intro
# django_intro> django-admin startproject your_project_name_here

# Let's test this out:

# Navigate into the folder that was just created. A new Django project has just been created--let's run it!

# django_intro> cd your_project_name_here
# your_project_name_here> python manage.py runserver

# Open localhost:8000 in a browser window. Hooray for CLIs (command-line interfaces)!

# (Don't worry about the warning about unapplied migrations. It won't affect us for now, and we'll address it soon enough.)

# Press ctrl-c to stop the server. Open up the project folder in your text editor. (Take note of the folder structure so far!) We'll be updating some of these files shortly.

# For every app we want to add to our project, we'll do the following:

# your_project_name_here> python manage.py startapp your_app_name_here


# The apps in a project CANNOT have the same name as the project.

# In the text editor, find the settings.py file. It should be in a folder with the same name as our project. Find the variable INSTALLED_APPS, and let's add our newly created app:

# your_project_name_here/your_project_name_here/settings.py

INSTALLED_APPS = [
    'your_app_name_here', # added this line. Don't forget the comma!!
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]    # the trailing comma after the last item in a list, tuple, or dictionary is commonly accepted in Python

#  For these next few steps, we are creating the route "/" to be associated with a specific function. Trust for now--we'll break this down in greater detail in the next tab. In the urls.py file, add a URL pattern for your new app. (You can delete the current admin pattern, or just ignore it for now). You will need to add an import for your views file.

# your_project_name_here/your_project_name_here/urls.py

# from django.urls import path, include           # import include
# from django.contrib import admin              # comment out, or just delete
urlpatterns = [
    path('', include('your_app_name_here.urls')),	   
    # path('admin/', admin.sites.urls)         # comment out, or just delete
]

#  Next, let's create a new urls.py file in the your_app_name_here folder. Put the following code
# your_project_name_here/your_app_name_here/urls.py

# project_name/project_name/urls.py

from django.urls import path, include
    
urlpatterns = [
    path('', include('app_name.urls')),
]

# Routing with Parameters
# Objectives:
# Learn how to capture variables from the url
# In this module, we will look into how Django interprets a request with varying values.

# Learn more from the documentation.

# Here are a few examples, to demonstrate the syntax:

some_project/some_app/urls.py
urlpatterns = [
        path('bears', views.one_method),                        # would only match localhost:8000/bears
        path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
        path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
        path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown
]
# The corresponding functions would then look like this:

some_project/some_app/views.py
def one_method(request):                # no values passed via URL
    pass                                
    
def another_method(request, my_val):	# my_val would be a number from the URL
    pass                                # given the example above, my_val would be 23
    
def yet_another(request, name):	        # name would be a string from the URL
    pass                                # given the example above, name would be 'pooh'
    
def one_more(request, id, color): 	# id would be a number, and color a string from the URL
    pass                                # given the example above, id would be 17 and color would be 'brown'



# Response Types
# In Django, there are many different ways we can return a response.  We will look into returning a HTML template in the next lesson, for now let's focus on these.

# HttpResponse: Can be used to pass a string as a response.
# Redirect: Used to navigate to a different view method, before a final response is sent to the client. ***Note*** Even though we don't include the first / in our project urls.py file, when redirecting, you should provide the whole path, starting with the first /.
# JsonResponse: Used to return a JSON object
# urls.py

from django.urls import path
from . import views
urlpatterns = [
    path('', views.root_method),
    path('another_route', views.another_method),
    path('redirected_route', views.redirected_method
]copy
views.py

from django.shortcuts import HttpResponse, redirect # add redirect to import statement
from django.http import JsonResponse
def root_method(request):
    return HttpResponse("String response from root_method")
def another_method(request):
    return redirect("/redirected_route")
def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})

# Templates #
# Objectives:
# Organize template files properly within a Django project
# Learn the syntax for rendering a template in Django
# Practice passing data to the template
# Django requires each app to have its own templates folder. Within that folder, store all your HTML templates.




# Assuming we've got the folder structure set up properly, we can then render templates in our views.py file like so:

project_name/app_name/views.py
from django.shortcuts import render	# notice the import!
def index(request):
    return render(request, "index.html")
When we call the render function, our first argument will always be request, and the second argument will be a string indicating which html file to render.

# Passing Data to the Template
# With Django, we are able to pass data to the template via the render method.  We do this by passing a single dictionary whose keys will be the variable names available on the template. For example:

project_name/app_name/views.py                               
from django.shortcuts import render
    
def index(request):
    context = {
        "name": "Noelle",
        "favorite_color": "turquoise",
        "pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)
project_name/app_name/templates/index.html

<h1>Info From Server:</h1>
<p>Name: {{name}}</p>
<p>Color: {{favorite_color}}</p>
<p>Pets</p>
<ul>
{% for pet in pets %}
    <li>{{pet}}</li>
{% endfor %}
</ul>
# Note: You cannot use square brackets with Django's template engine! Instead, use dot notation. 

# For example, array[0] becomes {{ array.0 }}

# Reminder: You cannot comment out template engine syntax with regular HTML comments (<!-- -->). (Check the documentation if you want to be able to comment it out properly)


# Static Files
# Objectives:
# Organize static files properly within a Django project
# Learn the syntax for referencing static content in templates
# The organization and behavior of static files is very similar to templates. Within each app, at the same level as our templates folder, we also need a folder called static. Then within that folder, we can save all of our static content (and further subdivide into js, css, and images folders as desired).

# In our templates, when we want to reference our static files, we'll first need to add a line indicating we want to use our static files:

# <!DOCTYPE html>
#    <html>
#     <head>
#       <meta charset="utf-8">
#       <title>Index</title>
#       {% load static %}		<!-- added this line -->

# Then we can reference any static files relative to their location within the folder called static:

# <!DOCTYPE html>
#   <html>
#     <head>
#       <meta charset="utf-8">
#       <title>Index</title>
#       {% load static %}
#       <link rel="stylesheet" href="{% static 'css/style.css' %}">    
#       <script src="{% static 'js/script.js' %}"></script>
#     </head>
#     <body>
#     	<img src="{% static 'images/image.jpg' %}" />
#     </body>

# GET vs. POST Requests #

# Objectives:
# Learn how to handle GET requests in Django
# Learn how to handle POST requests in Django
# Learn about CSRF tokens and why we use them
# A Django view method will be called regardless of the type of HTTP Request method that was made.  We can check the request method type being received, like so:

from django.shortcuts import render, redirect
def some_function(request):
    if request.method == "GET":
        print("a GET request is being made to this route")
        return render(request, "some_template.html")
    if request.method == "POST":
        print("a POST request is being made to this route")
        return redirect("/")

# Submitting Form Data
# As you've already seen, getting information from a user via forms is an extremely important part of web development. While forms can be submitted as GET or POST requests, we'll typically use them to submit POST requests.  In Django we will utilize the request.POST to access any form data that is submitted. (If the form is a GET request, that data can be accessed with request.GET.)

from django.shortcuts import render, redirect
def some_function(request):
    if request.method == "GET":
        print(request.GET)
    if request.method == "POST":
        print(request.POST)

# One more important thing to note is that any forms being submitted as POST requests must include a CSRF token. This token is used to prevent cross-site request forgery, a malicious kind of attack where a hacker can pretend to be another user and submit data to a site that recognizes that user. Adding a CSRF token to our forms allows Django to add a hidden input field and value that helps our server recognize genuine requests. If you forget to add this, Django will kindly provide a clear error message if you attempt to submit a form without a token. Add a token to each form with this line:

<form action="/some_route" method="post">
    {% csrf_token %}
    <p>Field One: <input name="one" type="text"></p>
    <p>Field Two: <input name="two" type="text"></p>
    <button type="submit">Submit</button>
</form>

# Remember that the names of the input fields from our form will be the keys we use to access the data in our server. So given the above form, we should be able to retrieve these values:

from django.shortcuts import render, redirect
def some_function(request):
    if request.method == "POST":
        val_from_field_one = request.POST["one"]
        val_from_field_two = request.POST["two"]

# POST Form Submission #

# Objectives:
# Learn the purpose of HTML forms
# Understand the action and method attributes of HTML forms
# Learn how to handle POST requests in our methods
# Learn how to access the form submission data in our server
# Up to this point, we have just been working with requests that display information from the server to the user. What if a request involves the client sending information to the server? The modern internet is user-driven; much of the actual content of a website is generated by the users of a website. How does a user provide content to a website? One word: forms. HTML forms are the way in which users are able to pass data to the back end of a website, where the data can then be processed and stored. Processing form data correctly is a huge part of what it takes to become a back-end developer.

# Let's create a new project called form_test with an app called form_app. We'll use this in the next few sections. Don't forget to add your app to settings.py!

# The first thing to do is to create a route and a method that will show a page with a form on it. Use the following snippets to get set up quickly:

# -----form_test/form_test/urls.py

from django.urls import path, include
    
urlpatterns = [
    path('', include('form_app.urls')),
]
form_test/form_app/urls.py
from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
]
# -----form_test/form_app/views.py

from django.shortcuts import render
def index(request):
    return render(request,"index.html")
Set up your template folder structure and create an index.html with the following form in the body:

# -----form_test/form_app/templates/index.html

<h1>Index Page</h1>
<h3>Create a User</h3>
<form action='/users' method='post'>
    {% csrf_token %}
    Name: <input type='text' name='name'>
    Email: <input type='text' name='email'>
    <button type='submit'>Create User</button>
</form>

# Once you've done the above, start up your server and visit localhost:8000/. you should see the index page with a form on it. Let's break down the critical parts of this form:

# action attribute
# This is the route that will process the form (not the one that shows the form--that's "/"). We'll set this up shortly.

# method attribute
# Our options are GET and POST; most likely, we'll want this to be a POST request (but if you don't set it, the default is GET)

# CSRF token
# This token is used to prevent cross-site request forgery, a malicious kind of attack where a hacker can pretend to be another user and submit data to a site that recognizes that user. Adding a CSRF token to our forms allows Django to add a hidden input field and value that helps our server recognize genuine requests. If you forget to add this, Django will kindly provide a clear error message if you attempt to submit a form without a token.

# input elements
# These are the parts of the form that actually gather data from the user. Check here for type options. Also check here for other form elements like select (dropdowns) and textarea. Each element should have a unique value for its name attribute.

# a way to submit the form
# This can either be <input type='submit'> or <button type='submit'>Submit</button>, but NOT <input type='button'>.

# Let's determine what should happen when the form is actually submitted. We indicated above, with the action attribute, that this POST request would be handled with the route /users, so let's add this to route to our app urls.py:

# -----form_test/form_app/urls.py

from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('users',views.create_user)
]
# Now that we have the route, let's set up the method:

# -----form_test/form_app/views.py

from django.shortcuts import render
def index(request):
    return render(request,"index.html")
        
def create_user(request):
    print("Got Post Info....................")
    print(request.POST)
    return render(request,"index.html")

# The above method will print out a message and the form data to the terminal. Run your server and try submitting a form. What do you see in the terminal? You should see something like this:

<QueryDict: {'csrfmiddlewaretoken': ['Yh5hBKVirURud5syD3nrsRdEoME766Cml3Z2ED1M9z5sIi7gxeak0LJzSCalfX9v'], 'name': ['John'], 'email': ['john@doe.com']}>

# Notice that the form data is being sent to our server in a dictionary. We see both the name and the email values that were input by the user. Let's modify our method to grab these values individually:

from django.shortcuts import render
def index(request):
    return render(request,"index.html")
        
def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    print(name_from_form)
    print(email_from_form)
    return render(request,"index.html")

# Restart your server and try submitting the form again. What do you see in the terminal now? Notice how we were able to extract just the name and the email.

# Accessing Data: request.POST['name_of_input']
# The name we gave to each HTML input was significant. On the server-side, we can access data that was input into a field from a user through the request.post dictionary by providing the name of the input as the key. To see the entire form, you can print request.post.

# Lastly, note that the type of anything that comes in through request.post will be a "string" no matter what. If you want that value to be identified as an actual number you'll have to type cast it.

# Finally, let's display this data on a new HTML page! We'll soon learn why it's not a great idea to render immediately as a response to a POST request, but more on that later.

# Make a new html file in your templates called show.html and add this code to the body:

# -----form_test/form_app/templates/show.html

<h1>Show Page</h1>
<h3>Info Submitted:</h3>
    <p>Name: {{ name_on_template }}</p>
    <p>Email: {{ email_on_template }}</p>
Next, modify your method in views.py:

# -----form_test/form_app/views.py

from django.shortcuts import render
def index(request):
    return render(request,"index.html")
        
def create_user(request):
    print("Got Post Info....................")
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
    	"name_on_template" : name_from_form,
    	"email_on_template" : email_from_form
    }
    return render(request,"show.html",context)

# Restart your server and submit the form! Do you see the data on the next page? Try adding more inputs and sending them over. It is important to become comfortable processing forms, so spend some time practicing.

# Objectives:
# Understand when to use a redirect
# Understand how to implement a redirect
# In the last reading, our form data was used right away on the next page, but this is not the best practice. We have to add a step between showing the form and displaying the form data. But why?

# Let's go back to our form_test project. Our create_user method is the one processing the POST request. Run the project and submit the form. Hit the refresh button in your browser--you should see a pop up like the one below. The warning explains that we are sending the same form data to be processed again.

# While it's not a big deal yet, imagine our method was inserting a user into the database, or processing a payment. Clicking continue would add that user to the database again, or process a payment twice. That would be no good!

# To avoid this, we need to change the way we process forms from being a two-step process to the three-step process. The flow will end up looking like this:

# Set up a route and method that will render a template to show the form
# Set up a route and method to process the form data that will redirect
# Set up a route and method that will render a template indicating the form was successfully processed
# Try changing your form_test project to follow the three steps. In addition to the following changes, make a success.html file that will display a success message to the user.

# -----form_test/form_app/urls.py

from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('create_user', views.create_user),
    path('success', views.success)
]
# ------form_test/form_app/views.py

from django.shortcuts import render, redirect # don't forget to import redirect!
def index(request):
    # this is the route that shows the form
    return render(request,"index.html")
def create_user(request):
    # this is the route that processes the form
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
        "name_on_template" : name_from_form,
        "email_on_template" : email_from_form
    }
    return redirect("/success")
def success(request):
    # this is the success route
    return render(request,"success.html")

# Now when we submit a form and hit refresh, we no longer receive the warning. Now, however, we've run into a new problem: we cannot send context over in a redirect, and once we redirect the form data is lost! Read on to learn one way we are able to hold on to, or persist data, across multiple requests!

# Session
# Objectives:
# Introduce the concept of state
# Introduce the need for persistence
# Learn about sessions in the context of web development
# Learn how Django handles session
# What are your thoughts on why our form data is gone after we redirect?

# Remember back to algorithms and the Python Fundamentals chapter--when we had several functions in the same file, did they know anything about each other? Nope! It is no different here--each method that is handling a route doesn't know anything about any of the other routes.

# Here's the thing about the HTTP request/response cycle: it is stateless. That means that each request/response cycle is independent and ignorant of all other requests, before or after. Because we made a second request (by redirecting) after the client posted data in the form, the browser only knows about the second request we made (in our case, the GET request to the "/success" route). Because the form data was part of the first request, the second request has no access to it.

# But certainly this is not our experience in the real world--when we go shopping online, the site seems to remember who we are, what items are in our shopping cart, etc. (Even other sites know what we've been shopping for! Creepy, right?) This is because many sites make use of persistent data storage! One form of persistence is session.

# What is Session?
# With session, we can establish a relationship with the client by saving, or writing, certain valuable pieces of data for use in future cycles. By reading that data we've stored in previous cycles, this opens up a new world of user experience. With session, the user can have a conversation of sorts with a website, where a user makes decisions that can be tracked so the server can create a more cohesive user experience.

# In a given process (HTTP request/response), we can manage data (search terms and search results for instance) that outlives the process that generated it. This data is called state. State allows our site to "know" a lot of useful information, like:

# Whether there is a user logged in
# Who the current user is
# What links a user has viewed previously
# We get to decide what to save about our clients--session is a tool for us, as developers, to use to our advantage. In the same way we create variables in our functions to help us solve problems, we keep state data in session to help us solve problems down the line, i.e. in subsequent HTTP requests.

# Persistent data storage helps us bridge the gap between a stateless protocol like HTTP with the stateful data generated through it. This is at the heart of the modern web and is heavily used by web developers around the world.

# Very shortly, we'll also discuss databases as another tool for persistent data storage. When we start incorporating a database into our projects, we'll consider what distinct roles each of these tools serve. We should not abuse the amount of information we store in session--store only what you need. Once we incorporate a database, we should be limiting what we store in session.

# A Note on Cookies
# You've probably heard of the term cookies before. Some frameworks, including Django, use cookies to store session data. Django uses secure hashing of session data to send a packet of information from server to client. This packet is known as a cookie. Once a client's browser has received this cookie, it writes the information contained in it to a small file on their hard drive.

# While hashed, cookies are not incredibly secure, so don't save anything private in them.

# Using Session in Django
# You may be itching to dismiss that warning about unapplied migrations. It's time! We'll talk about migrations more in depth when we integrate the database, but basically migrations help manage the state of our database, including creating and updating any tables. Django utilizes the database to manage sessions, so we'll need to update our database to allow for it to start maintaining session data for us. To do this, we'll run the following command from our terminal:

# -----(djangoPy3Env) project_name> python manage.py migrate

Excellent. Not only does that annoying warning disappear, but now session is available to us as well (as seen in that last line: Applying sessions.0001_initial... OK).

To use session, we can refer to it in our views.py file. Session is a dictionary to which we can add and retrieve values via keys, like so:

# ----

def some_function(request):
    request.session['name'] = request.POST['name']
    request.session['counter'] = 100
# We can also access session directly in our Django templates. Remember, though, that Django templates do not process square brackets, so we'll use dot notation instead:

<p>Name in session is: {{request.session.name}}</p>


Useful session methods:
request.session['key']
# This will retrieve (get) the value associated with 'key'
# request.session['key'] = 'value'
# Set the value that will be stored by 'key' to 'value'
'key' in request.session
# Returns a boolean of whether a key is in session or not
{{ request.session.name }}
# Use dot notation (.) to access request.session keys from templates since square brackets ([]) aren’t allowed there
del request.session['key']
# Deletes a session key if it exists, throws a KeyError if it doesn’t. Use along with try and except since it's better to ask for forgiveness than permission
# Note: If you are storing a list in session that is being modified (such as an append), you will need to save the session after the append, like so:
request.session['my_list'] = []
request.session['my_list'].append("new item")
request.session.save()

# Hidden Inputs
# Objectives:
# Learn about hidden inputs
# Learn how to add hidden inputs to a form
# Hidden input fields are form fields that are hidden from the user. Hidden input is used, along with other input elements, to transfer information between different pages.

# A hidden input is just an ordinary input element, but has no visual representation in the rendered HTML.

<input type="hidden" name="action" value="register">
# There are multiple ways we can make use of the hidden input field. In this tab, we are going to look at just one example. Suppose we have two forms within our index page:

<form method="post" action="/process">
    {% csrf_token %}
    <input type="hidden" name="which_form" value="register">
    <input type="text" name="first_name">
    <input type="text" name="last_name">
    <input type="text" name="email">
    <input type="password" name="password">
    <input type="submit" value="Register">
</form>
<form method="post" action="/process">
    {% csrf_token %}
    <input type="hidden" name="which_form" value="login">
    <input type="text" name="email">
    <input type="password" name="password">
    <input type="submit" value="Login">
</form>
# Notice that both forms submit their data to the POST /process route. How will we know which form was submitted? Each of the forms also has a hidden input with the same name, but different values. In this example, we are using the name "which_form".

# In the POST /process route, we could do something like this to process appropriately depending on which form was submitted:

if request.POST['which_form'] == 'register':
  //do registration process
elif request.POST['which_form'] == 'login':
  //do login process

# But know that, even though hidden inputs are invisible to the user, it is actually very visible in the page's source. That means other users can still see and change the values you set in the hidden input. So be very careful in choosing what data you store in there as value, and set appropriate actions if a user tries to change or remove it.

# Models in the MTV (MVC) Structure
# Objectives:
# Understand why Models are a separate component of the MTV (MVC) architecture
# Learn how to build a Django model
# The Why
# Let's get started using the ORM! Models are the M of the MTV architecture. Remember that the goal of modularizing is to separate our code so that each part has a specific purpose.

# The purpose of models is to do all the work of interfacing with the database, whether retrieving information from or putting information into it. The phrase skinny controllers and fat models is often used to describe this design pattern:

# As a general rule, any heavy logic, including database queries, should be performed by the Model. If a controller (in Django, that's the views.py file) needs to perform logic or get information from the database, it should use a Model method to do so.

# The How
# When we created our app, the Django CLI actually set up the models.py file for us. So far we have left it empty, but it's finally time to use it!

# Models are simply classes that map to our database tables. We'll start with just one table, and then talk about adding relationships over the next few modules and assignments. On the left is the ERD as we might have designed it in MySQL Workbench. On the right is the corresponding class we will actually write in our models.py file.


from django.db import models
    
class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
Let's break down the code in the models.py file a little bit:

# Why models.Model?
# First, notice we are inheriting from the models.Model base class. If you didn't have a chance to practice inheritance back in the OOP chapters, inheritance is an important OOP principle that allows us to write code in one class (parent) and then allow other classes (children) to inherit that same code without having to re-write it in the child classes.

# Practically speaking, this means that, even though we don't see additional code, Django's Model class provides a lot right out of the box. There's no way the Django developers could have anticipated all the different classes we as developers might create, but what they could anticipate was that we'd need classes, and that these classes would need to be created in our database, and they'd each need a primary key field. With that in mind, they created one generic parent Model class that contains these fields and functionalities.

# You'll notice, for example, that we do not need to type an id field into any of our classes--Django automatically adds a field called "id" to every class inheriting from models.Model and sets it to be an auto-incremented field. We also don't have to write a separate __init__ method for each class. Very shortly, we'll also see the models come pre-loaded with all the CRUD functionality so we aren't required to write out all the SQL statements.

# Other Fields
# Besides the id field, you'll notice that every field from our ERD has a corresponding line in our class. Each field is named and its type is specified. (We won't talk about relationship fields yet--those will come soon enough!) This is a great opportunity to begin reading documentation. The documentation will tell you what is required for each field type and what other options you can specify for each field. You can find a full list of allowed column types here. Below is a list of a few common types with some brief explanations to help you get started.

# # CharField
# # Any text that a user may enter. This has one required parameter, max_length, that is the maximum length of text that can be saved.
# # TextField
# # Like a CharField, but with no maximum length. Your user could copy the entire text of the Harry Potter series into the field and it would save in the database correctly.
# # IntegerField
# # Holds an integer value
# # FloatField
# # Holds a float value; this is good for numbers with potentially varying numbers of decimal places
# # DecimalField
# # This is a good field for a number with a fixed number of decimal places, like currency. There are 2 required parameters: max_digits refers to the total number of digits (before and after the decimal place), and decimal_places refers to how many decimal places.
# # BooleanField
# # Holds a boolean value
# # DateTimeField
# # Used for a combination of a specific date and time. This field can take two very useful optional parameters. Setting the auto_now_add argument to True adds the current date/time when an object is created. Setting auto_now=True automatically updates any time the object is modified.

# Migrations
# Objectives:
# Learn how to create a database and table(s) in SQLite based on our model(s)
# Understand what migrations do
# Now that we've set up our models, it's time to create an actual database with some tables! Luckily, Django can do the whole job for us with minimal code.

# To do this, (basically the equivalent of forward engineering in MySQL Workbench), we are going to run a couple of commands from the terminal.

#   > python manage.py makemigrations
#   > python manage.py migrate
# makemigrations is a kind of staging. When this command runs, Django looks through all our code, finds any changes we made to our models that will affect the database, and then formulates the correct Python code to move on to the next step. Note that if this step has errors, the next step will not work, so you will need to fix any errors before you can move on to migrating.

# migrate actually applies the changes made above. This step is where the SQL queries are actually built and executed.

# The migration process is split into two steps so that Django can check and make sure you wrote code it can understand before moving on to the next step.

# A Few Notes:
# Never delete migration files and always makemigrations and migrate anytime you change something in your models.py files – that's what updates the actual database so it reflects what's in your models.
# For now we are going to be using SQLite, a SQL database that comes pre-packaged with Django. It is best used in a development environment because it is stored as local memory in a file and as such is very fast. It is generally not recommended for use once our application is ready for production. Luckily, changing what kind of database we are using is quite simple. In the deployment section, we'll learn how to switch to a MySQL database.
# Django ORM models and queries will always be the same no matter which database we are using.

# Django Shell

# Objectives:
# Learn what the Django Shell is
# Learn how to import models into the shell
# Before tying models directly into our web applications, we're going to take a minute to open the Django shell to interact with our models and practice writing queries using Django's ORM.

# To use the shell, we'll run the following command in our terminal from our project's root directory (where our manage.py file is located):

# > python manage.py shell

# Once we're in the shell, we can access all of our functions and classes in our files. To do so, we just need to specify which modules (files) we need. Since we are interested specifically in working with our models, let's import them:

# >>> from your_app_name_here.models import *
# We will need to run this import every time we start the shell.

# Caution:  Since models.py contains the classes you wrote, importing everything in models.py is okay, but generally when you're importing other libraries/modules, the Django community discourages the practice of importing all (*). A good explanation can be found here: https://stackoverflow.com/questions/2360724/what-exactly-does-import-import. 

# Viewing the Database
# We can always use the shell to view the data in our database, but sometimes it can be frustrating to figure out how objects map to rows in a table. If you find the shell too frustrating to navigate, you can use a program called DB Browser for SQLite to view your database tables.

# ORM CRUD Commands
# Objectives:
# Learn/have a reference for basic ORM CRUD (Creating, Reading, Updating, and Deleting) commands
# Now that you have imported your models, let's start talking queries! This module is a little bit long--spend just a few minutes reading through to get familiar with what we're about to do. Just like we learned INSERT, SELECT, UPDATE, and DELETE statements in MySQL, we'll need methods that have the same functionality as those query commands.

# Once you've spent just a few minutes reviewing CRUD in this module, jump into the Users assignment! Use this module as a guide to practice each of the queries in the shell. Remember, the best way to learn is by doing!

# While SQL understands data in terms of tables and rows, in Django we'll refer to our data in terms of classes and class instances. Each row of data is an instance of the associated class. Even though a class instance is more than a dictionary, we can still think of an instance kind of like a dictionary, where our class's field names are the keys, and the actual data from our database are the values.

# Creating a new record

ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)

# Reading existing records

# Methods that return a single instance of a class

ClassName.objects.first() - gets the first record in the table
ClassName.objects.last() - gets the last record in the table
ClassName.objects.get(id=1) - gets the record in the table with the specified id
# this method will throw an error unless only and exactly one record matches the query
Methods that return a list of instances of a class
ClassName.objects.all() - gets all the records in the table
ClassName.objects.filter(field1="value for field1", etc.) - gets any records matching the query provided
ClassName.objects.exclude(field1="value for field1", etc.) - gets any records not matching the query provided
Updating an existing record
c = ClassName.objects.get(id=1)
c.field_name = "some new value for field_name"
c.save()

# Deleting an existing record

c = ClassName.objects.get(id=1)
c.delete()

# Other helpful methods

# Displaying records

ClassName.objects.get(id=1).__dict__ - shows all the values of a single record as a dictionary
ClassName.objects.all().values() - shows all the values of a QuerySet (i.e. multiple instances)

# Ordering records

ClassName.objects.all().order_by("field_name") - orders by field provided, ascending
ClassName.objects.all().order_by("-field_name") - orders by field provided, descending

# To take a deeper dive into any of these commands, keep scrolling. For the next few assignments, we'll be running all these commands in the shell. Once we go full stack, we will utilize these queries in our views.py file. The examples below utilize this model:

class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# CREATING
# To add a new record to a table:
# ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)
# SQL Equivalent: "INSERT INTO tablename (field1, field2) VALUES ('value for field1', 'value for field2');"
# The create method returns an instance of the model with the values that were just added. This means that if we wanted to do something with the instance after creating in our database, we could set a variable and use it like so:

newly_created_movie = Movie.objects.create(title="The Princess Bride",description="the best movie ever",release_date="1987-09-25",duration=98)
print(newly_created_movie.id)	# view the new movie's id

# Another way to add a row to our database is by creating an instance of the class (think back to the OOP section) and saving it, like so:

newly_created_movie = Movie(title="The Princess Bride",description="the best movie ever",release_date="1987-09-25",duration=98)
newly_created_movie.save()

# By default, all fields in our models are non-nullable, meaning all fields are required upon creation. If you want to change this default behavior, check out Django's documentation on the null property.

# READING
# There are several ways that we might want to retrieve records from the database.

# Multiple Records
# There are several different methods that will return multiple records (or lists of instances).

# All
# To get all the rows from a given table:

ClassName.objects.all()

# SQL Equivalent: "SELECT * FROM tablename;"
# The all method returns a list (technically a QuerySet) of instances of the model.

all_movies = Movie.objects.all()
Filter (WHERE)

# To specify criteria for retrieving rows from a given table:

ClassName.objects.filter(field1="value to match", field2="another value", etc.)

# SQL Equivalent: "SELECT * FROM tablename WHERE field='value to match' AND field2='another value';"
# The filter method also returns a list (technically a QuerySet) of instances of the model.  

some_movies = Movie.objects.filter(release_date='2018-11-16')
Exclude (WHERE NOT)

# To specify criteria for filtering out records to retrieve:

ClassName.objects.exclude(field1="value to match", field2="another value", etc.)

# SQL Equivalent: "SELECT * FROM tablename WHERE NOT (field='value to match' AND field2='another value');"
# The exclude method also returns a list (technically a QuerySet) of instances of the model.  

other_movies = Movie.objects.exclude(release_date='2018-11-16')

# When we have a list of instances, we can iterate through that list and view each instance and its values:

for m in all_movies:    # m represents each movie instance as we iterate through the list
    print(m.title)	# that means m has all the properties of the Movie class, including title, release_date, etc.

# Single Records
# There are also several different methods that will return a single instance of a class.

# Get
# To get a specific row from the table, specify a field and value.

ClassName.objects.get(field1="unique value")
SQL Equivalent: "SELECT * FROM tablename WHERE field1='unique value' LIMIT 1;"
The get method returns a single instance of the model.

# one_movie = Movie.objects.get(id=7)
# If our specified value(s) finds no matching results or more than one matching result from the database, we will get an error. This is why we should really only use fields that we know will be unique, with values that we are certain are in the database. For this reason, id is the most common field to use with get.

# First
# To get the first row from the table:

ClassName.objects.first()
# SQL Equivalent: "SELECT * FROM tablename ORDER BY id LIMIT 1;"
# The first method returns a single instance of the model. If no order is specified before calling the first method, the data is ordered by the primary key.

first_movie = Movie.objects.first()
Last
# To get the last row from the table:

ClassName.objects.last()
# SQL Equivalent: "SELECT * FROM tablename ORDER BY id DESC LIMIT 1;"
# The last method returns a single instance of the model. Again, if no order is specified before calling the last method, the data is ordered by the primary key.

last_movie = Movie.objects.last()

# When we are working with a single instance, we can access any of the instance's values with dot notation. For example:

print("Movie 7", one_movie.title)
print("First movie", first_movie.release_date)
print("Last movie", last_movie.description)

# UPDATING
# In order to update an existing record, we first need to obtain the instance of the record we want to modify and then use the save method to commit those changes to the database. For example:

movie_to_update = Movie.objects.get(id=42)	# let's retrieve a single movie,
movie_to_update.description = "the answer to the universe"	# update one/some of its field values
movie_to_update.title = "The Hitchhiker's Guide to the Galaxy"
movie_to_update.save()	# then make sure all changes to the existing record get saved to the database

# The equivalent SQL statement would be:

# "UPDATE tablename SET field1='new value', field2='new value' WHERE id=id_value;"
# DELETING
# In order to delete an existing record, we again need to obtain the instance of the record and then use the delete method. For example:

movie_to_delete = Movie.objects.get(id=2)	# let's retrieve a single movie,
movie_to_delete.delete()	# and then delete it
The equivalent SQL statement would be:

# "DELETE FROM tablename WHERE id=2;"
# Helpful Tip
# You've probably noticed in the shell that printing whole objects just results in something like <Movie Object (1)>, which is not particularly helpful. To change how our models display, we can override the __str__ method in the class. This is pretty handy and shows how we can leverage some of Python's magic methods to make our lives easier.

class Movie(models.Model):
    # fields removed for brevity
    def __str__(self):
        return f"<Movie object: {self.title} ({self.id})>"
# OPTIONAL: iPython
# Also, if you would like, you could also install iPython (pip install ipython). This replaces the default shell with a prettier one (TAB indent works, line numbers, syntax highlighting, etc).