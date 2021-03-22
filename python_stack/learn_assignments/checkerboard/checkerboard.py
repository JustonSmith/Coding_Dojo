from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', x = 8, y = 8, color1 = 'red', color2 = 'black')

@app.route('/<y>')
def down(y):
    return render_template('index.html', x = 8, y = int(y), color1 = 'red', color2 = 'black')

@app.route('/<x>/<y>')
def down_and_across(x, y):
    return render_template('index.html', x = int(x), y = int(y), color1 = 'red', color2 = 'black')

@app.route('/<x>/<y>/<color1>,')
def color_1(x, y, color1)
    return render_template('index.html', x = 8, y = int(y), color1 = color1 , color2 = 'black')

@app.route('/<x>/<y>/<color1>/<color2>')
def color_2(x, y, color1, color2):
    return render_template('index.html', x = 8, y = int(y), color1 = color1, color2 = color2)
    
if __name__ == "__main__":
    app.run(debug = True)


