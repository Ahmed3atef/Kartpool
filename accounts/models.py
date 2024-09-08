from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    karma_points = models.IntegerField(default=0)

    def add_karma_points(self, points):
        self.karma_points += points
        self.save()

    def __str__(self):
        return self.username