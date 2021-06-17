from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'secretkey'

@app.route('/')
def index():
    # initialize session values:
    if 'number' not in session:
        session['number'] = random.randrage(0,101)
    if 'number_of_guesses'not in session:
        session['number_of_guesses'] = 0
    if 'state' not in session:
        session['state'] = 'empty'
    if 'user_guess' not in session:
        session['user_guess'] = 0
    if 'current_guess' not in session:
        session['current_guesses'] = ''
    return render_template('index.html')

@app.route('/game', methods = ['POST'])
def game():
    # keep track of how many guesses:
    session['number_of_guesses'] += 1
    if session ['number of guesses'] == 5:
        session['state'] = "You Lose! Try Again. . . "
        return redirect('/')

    # keep track of which numbers have already been guessed:
    session['current_guess'] += str(request.form['user_guess']) + ", "
    session['user_guess'] = request.form['user_guess']

    # check if guess is higher, lower or equal to the random number:
    if int(session['user guess']) == session['random_number']:
        session['state'] = "win"
    if int(session['user guess']) < session['random_number']:
        session['state'] = "guess_higher "
    if int(session['user guess']) > session['random_number']:
        session['state'] = "guess_lower"
    

    @app.route('/reset')
    def reset():
        # Reset session information
        session['random_number'] = random.randrange(0,101)
        session['number_of_guesses'] = 0
        session['state'] = "empty"
        session['user_guess'] = 0
        session['current_guesses'] = ""
        return redirect('/')

    if __name__ == "__main__":
        app.run(debug = True)

