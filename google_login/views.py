from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'name': request.user.get_full_name() or request.user.username,
        'user': request.user,
        'events': []  # You can populate this with actual calendar events later
    }
    return render(request, "home.html", context)

@login_required
def profile(request):
    context = {
        'name': request.user.get_full_name() or request.user.username,
        'user': request.user,
    }
    return render(request, "profile.html", context)

@login_required
def settings(request):
    context = {
        'name': request.user.get_full_name() or request.user.username,
        'user': request.user,
    }
    return render(request, "settings.html", context)

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, "signup.html")

from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            next_url = request.GET.get('next', '/')
            return HttpResponseRedirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    context = {
        'google_login_url': '/accounts/google/login/',
        'signup_url': '/signup/',
        'next': request.GET.get('next', '/')
    }
    return render(request, "login.html", context)

def user_logout(request):
    logout(request)
    return render(request, "logout.html")

def logout_confirm(request):
    logout(request)
    return HttpResponseRedirect('/login')

def data(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return HttpResponseRedirect('/login')