from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MyUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    preferences = models.TextField(null=True)
    otp = models.SmallIntegerField(null=True)
    box = models.ForeignKey('game.Box', on_delete=models.SET_NULL, null=True)
    box_owner = models.BooleanField(default=False, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']
    objects = MyUserManager()

    def __str__(self):
        return self.email


class PasswordReset(models.Model):
    new_password = models.CharField(max_length=255)
