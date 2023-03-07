from django.shortcuts import render
from django.shortcuts import render, redirect
from django.db.models import Q

# Create your views here.

def set(request):
    response = render(request, 'setcookie.html')
    response.set_cookie('favorite', 'cheese cake')
    return response


def get(request):
    if 'favorite' in request.COOKIES.keys():
        favorite = request.COOKIES['favorite']
    else:
        favorite = 'No favorite'

    return render(request, 'getcookie.html', {'favorite': favorite})


def delete(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('favorite')
    return response


def session_set(request):
    # Store a value in the session
    request.session['special'] = '235%'
    return render(request, 'my_session.html', {'action': 'set'})

def session_get(request):
    # Retrieve a value from the session
    print(f"......{request.session.session_key}.....")
    special = request.session.get('special')
    min_purchase = request.session.get('min_purchase')
    return render(request, 'my_session.html', {'action': 'get',
                                               'special': special})

def session_delete(request):
    # Remove a value from the session
    del request.session['special']

    return render(request, 'my_session.html', {'action': 'delete'})