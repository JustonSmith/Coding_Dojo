from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.utils import redirect
from MySQLconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-] + @[a-zA-Z0-9._-] + .[a-zA-z]+$')
app = Flask(__name__)
bcrypt = Bcrypt
app.secret_key = "secret"




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard') #show
def thoughts():
    if 'user_id' not in session:
        flash('Must be logged in to access this page.')
        return redirect('/')
    user_id = session['user_id']
    mysql = connectToMySQL('thoughts_schema')
    query = "SELECT * FROM users WHERE id = %(session_user_id)s"
    data = {
        'session_user_id' : user_id
    }
    user = mysql.query_db(query, data)
    print(user)
    print('-'*40)
    mysql = connectToMySQL('thoughts_schema')
    query = "SELECT thoughts.content, users.form_first_name AS sender FROM thoughts_schema.thoughts JOIN users ON thoughts.poster_id = users.id WHERE thoughts.poster_id = %(session_user_id)s"
    data = {
        'session_user_id' : user_id
    }
    user_thoughts = mysql.query_db(query, data)

    mysql = connectToMySQL('thoughts_schema')
    query = "SELECT id, form_first_name FROM users WHERE id != %(session_user_id)s"
    data = {
        'session_user_id' : user_id
    }
    other_users_not_logged_in = mysql.query_db(query, data)

    return render_template('thoughts.html', user = users[0], thoughts = user_thoughts, other_users = other_users_not_logged_in)

@app.route('/register', methods=['POST']) # registration route
def register():
    is_valid = True
    if len(request.form['form_first_name']) < 1:
        flash("First Name is required.")
        is_valid = False
    if len(request.form['form_last_name']) < 1:
        flash("Last Name is required.")
        is_valid = False
    if not EMAIL_REGEX.match(request.form['form_email']):
        flash("Invalid Email Address.")
        is_valid = False
    if len(request.form['form_password']) < 8:
        is_valid = False
        flash("invalid password")
    else:
        mysql = connectToMySQL('thoughts_schema')
        query = "SELECT * FROM users WHERE form_email = %(email_from_form)s;"
        data = {
            'email_from_form': request.form['form_email']
        }
        user = mysql.query_db(query, data)
        if len(user) > 0:
            flash("email already exists")
            is_valid = False
    if request.form['form_password'] != request.form['form_confirm']:
            flash ("passwords do not match")
            is_valid = False
    if is_valid == False:
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['form_password'])
        mysql = connectToMySQL('thoughts_schema')
        query = "INSERT INTO users (form_first_name, form_last_name, form_email, form_password) VALUES (%(f_name)s, %(l_name)s, %(email)s, %(hashed_pw)s);"
        data = {
        'f_name': request.form['form_first_name'],
        'l_name': request.form['form_last_name'],
        'email': request.form['form_email'],
        'hashed_pw': pw_hash
        }
        user_id = mysql.query_db(query, data)
        print(user)
        print("-"*40)
        session['user_id'] = user_id
        return redirect('/dashboard')

@app.route('/logout', methods = ['POST']) # logout route
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods = ['POST']) #login route
def login():
    mysql = connectToMySQL('thoughts_schema')
    query = "SELECT * FROM users WHERE form_email = %(email_from_form)s;"
    data = {
        'email_from_form': request.form['form_email']
    }
    user = mysql.query_db(query, data)
    print(user)
    print("-"*40)
    if len(user) > 0:
        if bcrypt.check_password_hash(user[0]['form_password'], request.form['form_password']) == True: 
            session['user_id'] = user[0]['id']
            return redirect('/dashboard')
        else:
            flash("Invalid email/password combination")
            return redirect('/')
    else:
            flash("Email not in database.")
            return redirect('/')

@app.route('/posts/<post_id>/delete', methods=['POST'])
def delete_post(post_id):
    mysql = connectToMySQL('private_wall')
    query = "DELETE FROM thoughts_schema.thoughts WHERE id = %(message_id_from_browser)s;" 
    data = {
        'message_id_from_browser': post_id
    }
    user_thoughts = mysql.query_db(query, data)
    return redirect('/dashboard')

@app.route('/posts', methods = ['POST'])
def add_post():
    is_valid = True
    if len(request.form['content'] < 5):
        flash ("Thought required.")
        is_valid = False
    if is_valid == False:
        return redirect('/')
    else:
    mysql = connectToMySQL('thoughts_schema')
    query = "INSERT INTO thoughts_schema.thoughts ('content', 'poster_id') VALUES ('%(content)s,%(poster_id)s);"
    data = {
        'content': request.form['content'],
        'poster_id': session['user_id'],
    }
    user_thoughts = mysql.query_db(query, data)
    print()
    return redirect('/dashboard')

    if __name__ == "__main__":
        app.run(debug=True)
