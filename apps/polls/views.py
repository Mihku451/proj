from math import floor
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, HttpResponse

from apps.polls.models import Exercise, Question, Answer


def index(req):
    return render(req, "index.html")
