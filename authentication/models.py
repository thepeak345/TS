from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MyUserManager
from django import forms
from game.models import Box


class CustomUser(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    preferences = models.TextField(null=True)
    otp = models.SmallIntegerField(null=True)
    box = models.OneToOneField(Box, on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()


    def __str__(self):
        return self.email


class PasswordReset(models.Model):
    new_password = models.CharField(max_length=255)

