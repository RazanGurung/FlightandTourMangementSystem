from django.db.models import Q
from django.shortcuts import redirect
from management.models import USER
from django.contrib import messages


class Authenticate:

    def valid_user(function):
        def wrap(request):
            try:
                USER.objects.get(Q(email=request.session['email']) & Q(password=request.session['password']))
                return function(request)


            except:
                messages.warning(request, "please login....")
                return redirect("/login")
        return wrap
