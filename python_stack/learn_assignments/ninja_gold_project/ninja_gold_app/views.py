

# Create your views here.

from django.shortcuts import render,  HttpResponse, redirect
import random
import datetime

# Create your views here.
def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return render(request, 'index.html')

def home(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []
    return render(request, 'index.html')

def process(request):
    if request.method == "POST":
        if request.POST['action'] == "farm":
            print "* * * * * FARM * * * * *"
            earnings = random.randrange(10, 20)
            request.session['gold'] += earnings
            request.session['activities'].append(
                'Earned ' + str(earnings) + ' gold from the farm! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
            if len(request.session['activities']) >= 8:
                request.session['activities'].pop(0)
            return redirect('/')
        elif request.POST['action'] == "cave":
            print "* * * * * CAVE * * * * *"
            earnings = random.randrange(5, 10)
            request.session['gold'] += earnings
            request.session['activities'].append(
                'Earned ' + str(earnings) + ' gold from the cave! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
            if len(request.session['activities']) >= 8:
                request.session['activities'].pop(0)
            return redirect('/')
        elif request.POST['action'] == "house":
            print "* * * * * HOUSE * * * * *"
            earnings = random.randrange(2, 5)
            request.session['gold'] += earnings
            request.session['activities'].append(
                'Earned ' + str(earnings) + ' gold from the house! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
            if len(request.session['activities']) >= 8:
                request.session['activities'].pop(0)
            print "======len=========",len(request.session['activities'])
            return redirect('/')
        elif request.POST['action'] == "casino":
            print "* * * * * CASINO * * * * *"
            earnings = random.randrange(-50, 50)
            request.session['gold'] += earnings
            if earnings < 0:
                request.session['activities'].append(
                    'Fleeced the Casino for ' + str(earnings) + ' gold. Nice! (' +
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
                )
                if len(request.session['activities']) >= 8:
                    request.session['activities'].pop(0)
                return redirect('/')
            else:
                request.session['activities'].append(
                    'Casino takes you for' + str(earnings) + ' gold. Bummer! (' +
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
                )
                if len(request.session['activities']) >= 8:
                    request.session['activities'].pop(0)
                return redirect('/')
    else:
        return redirect('/')