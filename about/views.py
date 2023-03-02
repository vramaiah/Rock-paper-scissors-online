from django.shortcuts import render, redirect

def index(request):
    """Home page for our site"""
    if request.user.is_authenticated:
        return redirect('game:lobby')
    else:
        return render(request, 'about/index.html')
