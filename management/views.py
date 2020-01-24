from django.shortcuts import render, redirect
from management.models import User


def home(request):
    return render(request, "index.html")
def login(request):
    return render(request, "login.html")
def signup(request):
    return render(request, "register.html")
def gallery(request):
    return render(request, "gallery.html")