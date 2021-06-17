



from flask import Flask, render_template, request, redirect
app = Flask (__name__)



@app.route('/')
def dojo_survey():
    return render_template("dojo_survey.html")

@app.route("/result", methods = ['GET'])
def result():
    print("ENHANCE")
    print(request.form)
    name = request.form['name']
    if name <= 2:
        flash(" Not a valid entry")
    location = request.form['location']
    if location <= 2:
        flash(" Not a valid entry")
    language = request.form['language']
    if language <= 2:
        flash(" Not a valid entry")
    comment = request.form['comment']
    else:
        return ("Sucessful entry")
    return render_template('results.html', name = name, location = location, language = language, comment = comment)

if __name__ == "__main__":
    app.run(debug = True)
