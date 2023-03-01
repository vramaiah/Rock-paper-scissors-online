from django.shortcuts import render

def index(request):
    """Home page for our site"""
    return render(request, 'about/index.html')
