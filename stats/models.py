from django.db import models

from django.contrib.auth.models import User

class UserProfile(models.Model):
    """A model to store game data about a player"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wins = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    ties = models.PositiveIntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.user.username}'s game profile"