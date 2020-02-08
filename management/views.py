from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from management.forms import destinationform, galleryform
from management.models import USER, Destination, Gallery
from management.Authenticate import Authenticate


def home(request):
    return render(request, "index.html")


def login(request):
    return render(request, 'login.html')


def loginpage(request):
    request.session['email'] = request.POST['email']
    request.session['password'] = request.POST['password']
    return redirect('/package_dashboard')


@Authenticate.withid
def Package_dashboard(request):
    dests = Destination.objects.all()
    return render(request, "package_dashboard.html", {'dests': dests})


def admin(request):
    return render(request, "adminlogin.html")


def create_package(request):
    if request.method == 'POST':
        destform = destinationform(request.POST, request.FILES)
        destform.save()
        return redirect("/create_package")
        return messages.SUCCESS
    else:
        destform = destinationform()
    return render(request, 'create_packages.html', {'destform': destform})


def package_edit(request, id):
    destin = Destination.objects.get(D_Id=id)
    return render(request, 'package_edit.html', {'destin': destin})


def package_update(request, id):
    dest = Destination.objects.get(D_Id=id)
    destform = destinationform(request.POST, request.FILES, instance=dest)
    destform.save()
    return redirect('/package_dashboard')


def package_delete(request, id):
    Destination.objects.get(D_Id=id).image.delete()
    dest = Destination.objects.get(D_Id=id)
    dest.delete()
    return redirect('/package_dashboard')


def gallery_dashboard(request):
    galls = Gallery.objects.all()
    return render(request, "gallery_dashboard.html", {'galls': galls})


def create_gallery(request):
    if request.method == 'POST':
        gal_form = galleryform(request.POST, request.FILES)
        gal_form.save()
        return redirect("/create_gallery")
    else:
        gal_form = galleryform()
    return render(request, 'create_gallery.html', {'gal_form': gal_form})


def gallery_edit(request, id):
    gal = Gallery.objects.get(G_Id=id)
    return render(request, 'gallery_edit.html', {'gal': gal})


def gallery_update(request, id):
    gal = Destination.objects.get(G_Id=id)
    gal_form = destinationform(request.POST, request.FILES, instance=gal)
    gal_form.save()
    return redirect('/gallery_dashboard')


def gallery_delete(request, id):
    Gallery.objects.get(G_Id=id).image.delete()
    gall = Gallery.objects.get(G_Id=id)
    gall.delete()
    return redirect('/gallery_dashboard')


def dashboard_client(request):
    users = USER.objects.all()
    return render(request, 'dashboard_client.html', {'users': users})


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
    galls = Gallery.objects.all()
    return render(request, "gallery.html", {'galls': galls})


def package(request):
    dests = Destination.objects.all()
    return render(request, "packages.html", {'dests': dests})


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
