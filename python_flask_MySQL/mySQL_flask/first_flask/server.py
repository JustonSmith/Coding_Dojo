from flask import Flask, render_template, redirect, request, session, flash
from MySQLConnection import connectToMySQL    # import the function that will return an instance of a connection
app = Flask(__name__)
app.secret_key = "its a secret"

@app.route("/")
def index():
    mysql = connectToMySQL('first_flask')	        # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html", all_friends = friends)

@app.route('/process', methods=[POST])
def add_friend_to_db():
    mysql = connectToMySQL("flask_friends")
    query = "INSERT INTO friends(first_name, last_name, occupation, created_at, updated_at) VALUES (%(fn)s, %(ln)s, %(occup)s, NOW(), NOW());"
    data = {
        "fn": request.form["fname"],
        "ln": request.form["lname"],
        "occup": request.form["occ"],
    }
    new_friend_id = mysql.query_db(query, data)
    return redirect("/")
    # if there are errors:
    # figure out a way to show the user what went wrong
        # else if there are no errors:
# code from above to actually insert user into the database

@app.route('/process', methods=['POST'])
def process():
    is_valid = True		# assume True
    if len(request.form['fname']) < 1:
    is_valid = False
    flash("Please enter first name")
    # display validation error
    if len(request.form['lname']) < 1:
    is_valid = False
    flash("Please enter last name")
    # display validation error
    if len(request.form['occ']) < 2:
    is_valid = False
    flash("Occupation should be at least 2 characters")
    # display validation error
    
    if not is_valid:    # if any of the fields switched our is_valid toggle to False
        return redirect('/')    # redirect back to the method that displays the index page
    else:               # if is_valid is still True, all validation checks were passed
    # add user to database
        flash("Friends sucessfully added")
        return redirect("/")
        # display success message
        # redirect to a method that displays a success pag


if __name__ == "__main__":
    app.run(debug=True)