from django.urls import path

from .import views

urlpatterns =[
    path('',views.home, name='index'),
    path("login",views.login, name='login'),
    path('signup',views.signup, name='register'),
    path('gallery',views.gallery, name='gallery')
]