"""defines URL patterns for the game"""

from django.urls import path

from . import views

app_name = 'game'
urlpatterns = [
    path('lobby/', views.lobby, name='lobby')
]