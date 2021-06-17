from flask import Flask, render_template, request, redirect, session, flash
from MySQLconnection import connectToMySQL
from flask_bcrypt import Bcrypt
app = Flask(__name__)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$')
bcrypt = Bcrypt(app)
app.secret_key = "secret"





### NOTES ### 

# ----- Be careful and concious of what you're 'naming' things. Keep track of your 'names' and how they interact between the DB, HTML and PY files. &()s can be called anything but must match later in data. Make lots of notes of where you need, when you need. USE PRINT AFTER YOUR FUNCTIONS. It's complex, not complicated. Make sure the stuff you know will run, runs first, then move on.  Lifting heavier up front will help your debugging process. ----- #






#_______GET REQUESTS_______#

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def thoughts():
    if 'user_id' not in session:
        flash('Must be logged in to access this page.')
        return redirect('/')
    user_id = session['user_id']
    mysql = connectToMySQL('thoughts_schema')
    query = "SELECT * FROM users WHERE id = %(session_user_id)s"
    data = {
        'session_user_id' : session['user_id']
    }
    user = mysql.query_db(query, data) ### FUNCTION ###

    mysql = connectToMySQL('thoughts_schema')
    other_users_not_logged_in = mysql.query_db("SELECT * FROM thoughts_schema.thoughts JOIN users ON users.id = thoughts.users_id;") ###FUNCTION ### ### OTHER USERS ### 

    mysql = connectToMySQL('thoughts_schema')
    likes = mysql.query_db("SELECT thoughts_id, COUNT(*) AS total_likes FROM likes WHERE thoughts_id IS NOT NULL GROUP BY thoughts_id;")### FUNCTION ### ### LIKES ###

    return render_template('dashboard.html', user_thoughts = other_users_not_logged_in, likes = likes)

        @app.route('/user') ### SHOW SINGLE USER'S THOUGHTS ON SEPERATE PAGE ### 
def get_users_thoughts():
    mysql = connectToMySQL('thoughts_schema')
    query = "SELECT * FROM thoughts.content JOIN users ON users.id AND thoughts ON thoughts.users_id WHERE thoughts.content = users.id;"

    return render_template('user.html')


    #________POST REQUESTS________#

@app.route('/register', methods=['POST']) ### REGISTRATION ROUTE ###  ### VALIDATIONS ###
def register():
    is_valid = True
    if len(request.form['first_name']) < 1:
        flash("First Name is required.")
        is_valid = False
    if len(request.form['last_name']) < 1:
        flash("Last Name is required.")
        is_valid = False
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address.")
        is_valid = False
    if len(request.form['password']) < 8:
        is_valid = False
        flash("invalid password")
    else:
        mysql = connectToMySQL('thoughts_schema')
        query = "SELECT * FROM users WHERE email = %(email_from_form)s;" ### DB QUERY ###
        data = {
            'email_from_form': request.form['email']
        }
        user = mysql.query_db(query, data) ### FUNCTION ###
        if len(user) > 0:
            flash("email already exists")
            is_valid = False
    if request.form['password'] != request.form['confirm']:
            flash ("passwords do not match")
            is_valid = False
    if is_valid == False:
        return redirect('/')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['password']) ### GENERATE PASSWORD HASH ### 
        mysql = connectToMySQL('thoughts_schema')
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(f_name)s, %(l_name)s, %(email)s, %(hashed_pw)s);" ### DB QUERY ###
        data = {
        'f_name': request.form['first_name'],
        'l_name': request.form['last_name'],
        'email': request.form['email'],
        'hashed_pw': pw_hash
        }
        user_id = mysql.query_db(query, data) ### FUNCTION ###
        print(user)
        print("-"*40)
        session['user_id'] = user_id
        session['username'] = request.form['first_name']
        return redirect('/dashboard')

@app.route('/logout', methods = ['POST']) ### LOGOUT ROUTE ###
def logout():
    session.clear()
    return redirect('/')

@app.route('/login', methods = ['POST']) ### LOGIN ROUTE ###
def login():
    mysql = connectToMySQL('thoughts_schema')
    query = "SELECT * FROM users WHERE email = %(email_from_form)s;" ### DB QUERY ###
    data = {
        'email_from_form': request.form['email']
    }
    user = mysql.query_db(query, data) ### FUNCTION ###
    print(user)
    print("-"*40)
    if len(user) > 0:
        if bcrypt.check_password_hash(user[0]['password'], request.form['password']) == True: ### PASSWORD VALIDATION ###
            session['user_id'] = user[0]['id']
            session['username'] = user[0]['first_name']
            return redirect('/dashboard')
        else:
            flash("Invalid email/password combination")
            return redirect('/')
    else:
            flash("Email not in database.")
            return redirect('/')

@app.route('/posts/<thoughts_id>/delete', methods=['POST']) # <_> must mach in 3 places. <--- 1    ### DELETE THOUGHT ###
def delete_thought(thoughts_id): # <--- 2
    mysql = connectToMySQL('thoughts_schema')
    query = "DELETE FROM thoughts_schema.thoughts WHERE id = %(thoughts_from_browser)s;" ### DB QUERY ###
    data = {
        'thoughts_from_browser': thoughts_id # <--- 3
    }
    user_thoughts = mysql.query_db(query, data)
    return redirect('/dashboard')

@app.route('/posts/<thoughts_id>/like', methods= ['POST']) # <_> must mach in 3 places. <--- 1    ### LIKE THOUGHT ###
def like_thought(thoughts_id): # <--- 2
    mysql = connectToMySQL('thoughts_schema')
    query = "INSERT INTO thoughts_schema.likes (users_id, thoughts_id) VALUES (%(users)s, %(thoughts)s);" ### DB QUERY ###
    data = {
        'users': session['user_id'],
        'thoughts': thoughts_id # <--- 3
    }
    likes = mysql.query_db(query, data)
    print(likes)
    return redirect('/dashboard')

@app.route('/posts/<thoughts_id>/dislike', methods= ['POST']) #  <_> must mach in 3 places. <--- 1    ### DISLIKE THOUGHT ###
def dislike_thought(thoughts_id): # <--- 2
    mysql = connectToMySQL('thoughts_schema')
    query = "DELETE FROM thoughts_schema.likes WHERE users_id = %(users)s AND thoughts_id = %(thoughts)s;" ### DB QUERY ###
    data = {
        'users': session['user_id'],
        'thoughts': thoughts_id # <--- 3
    }
    dislikes = mysql.query_db(query, data)
    print(dislikes)
    return redirect('/dashboard')

@app.route('/posts', methods = ['POST']) ### ADD THOUGHT ###
def add_thought():
    is_valid = True
    if len(request.form['content']) < 5: ### VALIDATION ### 
        flash ("Thoughts required.")
        is_valid = False
    if is_valid == False:
        return redirect('/')
    else:
        mysql = connectToMySQL('thoughts_schema')
        query = "INSERT INTO thoughts_schema.thoughts (content, users_id) VALUES (%(content)s, %(poster_id)s);" ### DB QUERY ###
        data = {
        'content': request.form['content'],
        'poster_id': session['user_id'],
        }
        user_thoughts = mysql.query_db(query, data) ### FUNCTION ###
        print()
        return redirect('/dashboard')



if __name__ == "__main__":
    app.run(debug=True)
