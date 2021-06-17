from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("checkerboard.html", x = int(8), y = int(8))


@app.route('/4')
def checkerboard2():
    return render_template("checkerboard.html", x = int(4), y = int(4))


@app.route('/<x>/<y>')
def checkerboard3(x, y):
    return render_template("checkerboard.html", x = int(x), y = int(y))

# @app.route('/<x>/<y>/<color1>/color2')
# def checkerboard4(x, y, color1, color2):
#     return render_template("checkerboard.html", x = int(x), y = int(y))

if __name__ == "__main__":
    app.run(debug = True)


