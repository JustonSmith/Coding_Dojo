from flask import Flask, render_template, request, redirect, session, flash
from werkzeug.utils import redirect
from MySQLconnection import connectToMySQL
import re
from flask_bcrypt import Bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "its a secret"

# ________GET REQUESTS____________

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Must be logged in to access this page.')
        return redirect('/')

    user_id = session['user_id']
    # get the logged in user
    mysql = connectToMySQL('private_wall')
    query = "SELECT * FROM users WHERE id = %(session_user_id)s"
    data = {
        'session_user_id' : user_id
    }
    user = mysql.query_db(query, data)
    print(user)
    print('-'*40)

    # get the messages for the logged in user
    mysql = connectToMySQL('private_wall')
    query = "SELECT messages.content, users.form_first_name AS sender FROM private_wall.messages JOIN users ON messages.sender_id = users.id WHERE messages.receiver_id = %(session_user_id)s"
    data = {
        'session_user_id' : user_id
    }
    user_messages = mysql.query_db(query, data)

    # get all the users, except for the logged in user
    mysql = connectToMySQL('private_wall')
    query = "SELECT id, form_first_name FROM users WHERE id != %(session_user_id)s"
    data = {
        'session_user_id' : user_id
    }
    other_users_not_logged_in = mysql.query_db(query, data)

    return render_template('dashboard.html', user = user[0], messages = user_messages, other_users = other_users_not_logged_in)



# ___________POST REQUESTS_________________

@app.route('/register', methods=['POST'])
def register():
# validation
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
        # check to see if its unique(db,query)
        mysql = connectToMySQL('private_wall')
        query = "SELECT * FROM users WHERE form_email = %(email_from_form)s;"
        data = {
            'email_from_form': request.form['form_email']
        }
        user = mysql.query_db(query, data)
        # check the result for a match
        if len(user) > 0:
            # the email exists in the DB
            flash("email already exists")
            is_valid = False

    if request.form['form_password'] != request.form['form_confirm']:
            flash ("passwords do not match")
            is_valid = False

    # if passed the validations
    if is_valid == False:
        # False -- display errors, redirect to index.
        return redirect('/')

    else:   # True -- create the user, save in session, redirect to dashboard
            # create hashed password
        pw_hash = bcrypt.generate_password_hash(request.form['form_password'])
        mysql = connectToMySQL('private_wall')
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
        # save the id in session
        session['user_id'] = user_id
        return redirect('/dashboard')

@app.route('/logout', methods = ['POST'])
def logout():
    session.clear()
    return redirect('/')


@app.route('/login', methods = ['POST'])
def login():
    # check for user in DB
    mysql = connectToMySQL('private_wall')
    query = "SELECT * FROM users WHERE form_email = %(email_from_form)s;"
    data = {
        'email_from_form': request.form['form_email']
    }
    user = mysql.query_db(query, data)
    print(user)
    print("-"*40)
    # check the result for a match
    # if user
    if len(user) > 0:
        # the email exists in the DB
        # compare password
        if bcrypt.check_password_hash(user[0]['form_password'], request.form['form_password']) == True:
        # if match
        # login in the user 
            session['user_id'] = user[0]['id']
            return redirect('/dashboard')
    # or else
        else:
        # error message to index
            flash("Invalid email/password combination")
            return redirect('/')
    # no user
    else:
        #error message to index
            flash("Email not in database.")
            return redirect('/')


@app.route('/messages/<message_id>/delete', methods=['POST'])
def delete_message(message_id):
    mysql = connectToMySQL('private_wall')
    query = "DELETE FROM private_wall.messages WHERE id = %(message_id_from_browser)s;" 
    data = {
        'message_id_from_browser': message_id
    }
    user_messages = mysql.query_db(query, data)
    return redirect('/dashboard')

@app.route('/messages', methods = ['POST'])
def add_message():
    mysql = connectToMySQL('private_wall')
    query = "INSERT INTO private_wall.messages ('content', 'sender_id', 'receiver_id') VALUES ('%(content)s,%(user_id)s, %(receiver_id)s);"
    data = {
        'content': request.form['content'],
        'sender_id': session['user_id'],
        'receiver_id': request.form['receiver_id']
    }
    user_messages = mysql.query_db(query, data)
    print()
    return redirect('/dashboard')

if __name__ == "__main__":
    app.run(debug=True)