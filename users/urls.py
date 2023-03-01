"""defines URL patterns for users"""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Include default URLS
    path('', include('django.contrib.auth.urls')),
]