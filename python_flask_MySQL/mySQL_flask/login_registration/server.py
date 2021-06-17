from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.utils import redirect
from MySQLconnection import connectToMySQL
import re
app = Flask(__name__)
app.secret_key = "its a secret"
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/login', methods=["POST"])
def login():
    mysql = connectToMySQL("login_registration")
    query = "SELECT * FROM user WHERE email = %(username)s"
    data = {"username": request.form["email"]}
    get_user = mysql.query_db(query, data)
    print(get_user)
    if len(get_user) > 0:
        if bcrypt.check_password_hash(get_user[0]['password'], request.form['password']):
            session['id'] = get_user[0]['id']
            session['userid'] = get_user[0]['first_name']
            session['pw_hash'] = get_user[0]['password']
            session['logged_in'] = True
            flash("You have successfully logged in.")
            return redirect('/success')
    else:
        session['logged_in'] = False
        flash("Login failed. Have you registered?")
        return redirect('/')

@app.route('/logout', methods=["POST"])
def logout():
    session['logged_in'] = False
    flash("You have been logged out. ")
    return redirect('/')

@app.route('/register', methods=["POST"])
def register():
    is_valid = True
    if len(request.form['first_name']) <2:
        is_valid = False
        flash("invalid input")
    if len(request.form['last_name']) <2:
        is_valid = False
        flash("invalid input")
    if not EMAIL_REGEX.match(request.form['email']):
        is_valid = False
        flash("invalid email")
    if len(request.form['password']) < 8:
        is_valid = False
        flash("invalid password")
    if request.form['password_confirm'] != request.form['password']:
        is_valid = False
        flash ("passwords do not match")
    if not is_valid:
        return("/")
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print(pw_hash)
        mysql = connectToMySQL('login_registration')
        query = "INSERT INTO user (first_name, last_name, email, password, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": pw_hash 
            }
        flash ("valid registration")
        mysql.query_db(query,data)
        session['userid'] = request.form["first_name"]
        return redirect('/success')

@app.route('/success', methods=["GET"])
def success():
    mysql = connectToMySQL("login_registration")
    users = mysql.query_db('SELECT * FROM user')
    print(users)
    return render_template("/success.html")

if __name__ == "__main__":
    app.run(debug= True)


