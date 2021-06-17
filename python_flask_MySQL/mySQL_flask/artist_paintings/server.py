from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
app= Flask(__name__)
app.secret_key = 'secret'
bcrypt = Bcrypt(app)

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/dashboard")
def user_paintings():
    mysql = connectToMySQL("artist_paintings")
    query = ('SELECT * FROM users WHERE id = (%(user_id)s);')
    data = {
        "user_id": session['userid']
    }
    user = mysql.query_db(query, data)
    mysql = connectToMySQL("artist_paintings")
    magazines = mysql.query_db ("SELECT * FROM magazines JOIN users WHERE users.id = magazines.users_id;")
    return render_template("dashboard.html", users = user, magazines = magazines)



@app.route('/register', methods =['POST'])
def registration():
    is_valid = True
    if len(request.form['first_name']) < 2:
        is_valid = False
        flash("Must enter first name.")
    if len(request.form['last_name']) < 2:
        is_valid = False
        flash("Must enter last name.")
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid= False
        flash("Invalid email address.")
    if len(request.form['password']) < 8:
        is_valid = False
        flash("Password must contain 8 characters.")
    if request.form['password'] != request.form['confirm']:
        is_valid = False
        flash("Passwords do not match")
    mysql = connectToMySQL("artist_paintings")
    query = "SELECT * FROM users WHERE email= %(email)s;"
    data = {
        "email": request.form["email"],
        }
    user_email = mysql.query_db(query, data)
    if len(user_email) > 0:
        is_valid = False
        flash("Email already in database")
    if not is_valid:
        return redirect("/")

    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        mysql = connectToMySQL("artist_paintings")
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s);"
        data = {
            "first_name": request.form['first_name'],
            "last_name": request.form['last_name'],
            "email": request.form["email"],
            "password_hash": pw_hash ,
            }
        new_user = mysql.query_db(query, data)
        session['username'] = new_user
        session['userid'] = new_user
        print (new_user)
        flash("Registered successfully.")
        session
        return redirect('/dashboard')

@app.route('/login', methods = ["POST"])
def user_login():
    mysql = connectToMySQL("artist_paintings")    
    query = "SELECT * FROM users WHERE email = %(email)s;"
    data = {"email" : request.form["email"]}
    user_login = mysql.query_db(query, data)
    if len(user_login)> 0:
        if bcrypt.check_password_hash(user_login[0]['password'], request.form['password']):
            session['userid'] = user_login[0]['id']
            session['username'] = user_login[0]['first_name']
            return redirect('/dashboard')
        else:
            flash("Login Failed")
            return redirect('/')
    else:
        flash("Please provide valid login information.")
        return redirect('/')

