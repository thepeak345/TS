from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from .models import Box


class BoxForm(forms.ModelForm):
    class Meta:
        model = Box
        fields = ('is_closed', 'size')


class BoxTitle(forms.ModelForm):
    class Meta:
        model = Box
        fields = ('title', 'start_date', 'end_date')


class CodeboxForm(forms.Form):
    codebox = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(CodeboxForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.name
