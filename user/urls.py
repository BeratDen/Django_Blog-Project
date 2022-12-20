from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    # TODO: change method
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
]
