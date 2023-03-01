"""Defines URL patterns for pages describing the game"""

from django.urls import path

from . import views

app_name = "about"
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
]
