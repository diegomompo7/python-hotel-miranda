from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("rooms/", include("polls.urls")),
]