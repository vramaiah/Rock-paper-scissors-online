from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from stats.models import UserProfile

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank form
        form = UserCreationForm()
    else:
        # Process form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # Create user and their profile
            new_user = form.save()
            profile = UserProfile(user=new_user, wins=0, losses=0, ties=0)
            profile.save()
            # Log in user and redirect to home page
            login(request, new_user)
            return redirect('about:index')
    # Display a blank/invalid form
    context = {'form' : form}
    return render(request, 'registration/register.html', context)
