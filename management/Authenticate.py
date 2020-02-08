from django.db.models import Q
from django.shortcuts import redirect
from management.models import USER


class Authenticate:

    def withid(function):
        def login(request):
            try:

                USER.objects.get(Q(email=request.session['email']) & Q(password=request.session['password']))
                return function(request)

            except:
                return redirect("/login")

        return login
