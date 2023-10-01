from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from user.manager import CustomUserManager


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager()


class InvalidAccessToken(models.Model):
    token = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.token

