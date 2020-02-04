from django.shortcuts import render, redirect
from management.models import USER
from management.forms import userform
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from management.Authenticate import Authenticate


def home(request):
    return render(request, "index.html")


def login(request):
    return render(request, 'login.html')


@Authenticate.valid_user
def loginpage(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/dashboard')


def dashboard(request):
    return render(request, "dashboard.html")


def admin(request):
    return render(request, "adminlogin.html")


def signup(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('email') \
                and request.POST.get('password1') and request.POST.get('gender') and request.POST.get('dob'):
            register = USER()
            register.first_name = request.POST.get('first_name')
            register.last_name = request.POST.get('last_name')
            register.email = request.POST.get('email')
            register.password = request.POST.get('password1')
            register.gender = request.POST.get('gender')
            register.dob = request.POST.get('dob')
            register.save()
            return render(request, "login.html", {'register': register})
    else:
        return render(request, "register.html")


def gallery(request):
    return render(request, "gallery.html")


def package(request):
    return render(request, "packages.html")


def explore(request):
    return render(request, "explore.html")


def news(request):
    return render(request, "news.html")


def tips(request):
    return render(request, "tricks.html")


def rental(request):
    return render(request, "rental.html")


def dashboard(request):
    return render(request, "dashboard.html")
