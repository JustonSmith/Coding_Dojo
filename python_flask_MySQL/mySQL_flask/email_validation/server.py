
from flask import Flask, render_template, request, redirect, session, flash
from MySQLconnection import connectToMySQL
app= Flask(__name__)
app.secret_key = 'My super secret key'
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')

@app.route('/')
def newemail():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def display():
    if not EMAIL_REGEX.match(request.form['email_address']):
        flash("Invalid email address!") 
        return redirect ('/')
    else:
        mysql = connectToMySQL("email_schema")
        query = "INSERT INTO emails(email_address, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        data = {
            "email": request.form["email_address"],
            }
        email = mysql.query_db(query, data)
        flash("Valid email")
        return redirect('/display')


@app.route('/display')
def showall():
    mysql = connectToMySQL("email_schema")
    users = mysql.query_db('SELECT * FROM emails')
    print(users)
    return render_template("success.html", emails = users)




if __name__ == "__main__":
    app.run(debug= True)