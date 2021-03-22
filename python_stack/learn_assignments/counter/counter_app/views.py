from django.shortcuts import render

# Create your views here.

def index(request):
    if "count" not in request.session:
        request.session["count"] = 1
    else:    
        request.session["count"] += 1

    context = {
        'title' : 'Counter'
    }

    return render(request,"index.html", context)    

def view_count(request):
    if request.form["alter"]=="add":
        request.session["count"] += 1
    elif request.form["alter"]=="reset":
        request.session["count"] = 0

    return redirect("/")

def destroy(request):
    session.clear()
    return redirect("/")



if __name__=="__main__":
    app.run(debug=True) 