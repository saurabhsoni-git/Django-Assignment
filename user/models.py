from django.db import models
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.email} - {self.username} "