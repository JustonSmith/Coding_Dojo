# 
# 

# understanding_routing


from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/hello/<name>") 
def myName(name):
    print(name)
    return "Hello, " + name

@app.route("/Dojo")
def hello():
    return "Dojo "

@app.route("/say/<word>")
def say(word):
    print(word)
    return "Hi, " + word

@app.route("/repeat/<times_repeat>/<repeat_str>")
def repeat(times_repeat, repeat_str):
    string = repeat_str * int(times_repeat)
    return string

if @app.route !== @app.route('/'):
    or @app.route !== @app.route('hello/<name>')
    or @app.route !== @app.route('/dojo')
    or @app.route !== @app.route('say/word')
    or @app.route !== @app.route('/repeat/<times repeat>/<repeat_str')
    return "Sorry! No response. Try again."



if __name__ == "__main__":

    app.run(debug = True)