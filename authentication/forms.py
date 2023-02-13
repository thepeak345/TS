from django import forms


class SignUpForm(forms.Form):
    email = forms.EmailField()
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    firstname = forms.CharField(max_length=255)
    lastname = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class OtpForm(forms.Form):
    otp = forms.IntegerField()

