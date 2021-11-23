from math import floor

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from apps.polls.models import Exercise, Question, Answer


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        email = request.POST.get('email')

        password = request.POST.get('password')

        password2 = request.POST.get('password2')
        if password == password2:
            User.objects.create_user(username, email, password)
            return redirect("/")
    return render(request, "register.html")


def logout_view(request):
    logout(request)


def login(request):
    context = {}
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/")
    else:
        context['error'] = "Логин или пароль неправильные"
    return render(request, "login.html", context)


def index(request):
    return render(request, "index.html")


def create_exercise(req):
    return render(req, "create_exercise.html")


def register(request):
    return render(request, 'register.html')
