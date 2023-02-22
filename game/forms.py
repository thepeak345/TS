from django import forms
from django.contrib.auth import get_user_model

from .models import Box


class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ('is_closed', 'size')
