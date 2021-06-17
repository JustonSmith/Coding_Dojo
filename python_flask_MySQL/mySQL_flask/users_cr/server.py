from flask import Flask, render_template, redirect, request
from MySQLconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)
@app.route("/")
def index():
    mysql = connectToMySQL('users_schema')	        # call the function, passing in the name of our db
    users = mysql.query_db('SELECT * FROM users;')  # call the query_db function, pass in the query as a string
    print(users) #terminal
    return render_template("read(all).html", all_users = users)

@app.route("/users")
def users():
    return render_template("create.html")

@app.route("/add_user", methods = ["POST"])
def add_user():
    mysql = connectToMySQL('users_schema')

    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) WHERE id = (%(fn)s, %(ln)s, %(e)s, NOW(), NOW());"
    data = {
        "fn": request.form ["first_name"],
        "ln": request.form ["last_name"],
        "e": request.form ["email"]
    }
    mysql = connectToMySQL('users_schema')
    mysql.query_db(query, data)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)