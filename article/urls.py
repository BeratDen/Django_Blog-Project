from django.contrib import admin
from django.urls import path
from . import views


app_name = "article"

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add/", views.add, name="add"),
    path("article/<int:id>/", views.detail, name="article"),
    path("update/<int:id>/", views.update, name="update"),
    path("delete/<int:id>/", views.delete, name="delete"),
]
