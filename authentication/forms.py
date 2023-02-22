from django import forms
from django.contrib.auth import get_user_model
from .models import PasswordReset

User = get_user_model()


class SignUpForm(forms.Form):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.name


class LoginForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.name


class OtpForm(forms.Form):
    otp = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super(OtpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.name


class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('new_password',)

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.name
