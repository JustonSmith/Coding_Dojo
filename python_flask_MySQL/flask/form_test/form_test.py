# 
# 

# Form Test:

from flask import Flask, render_template, redirect
app = Flask(__name__)

from flask import Flask, render_template, request, redirect # don't forget to import redirect!
    
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    email = request.form['email']
    return redirect("/show")	# changed this line!
    
# adding this method
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("show.html")

app.route('/')
def index():
    print( 'in index', session['names'])
    return render_template('form_test.html', all_name = session['names'])


    app. route('/') # GET
    def index():
        return render_template('index.html')

    app.route('/process', methods = ['POST'])
    def process():
        print('in process')
        print(request.form['name'])

        if 'names' not in session:
            session ['names'] = []
        session ['names'].append (request.form ['name'])
        session.modified = True
        print('in process', session['names'])
        return redirect('/')







    if __name__ == "__main__":
        app.run(debug = True)